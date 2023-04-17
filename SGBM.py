#!/usr/bin/python

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
from sklearn.preprocessing import normalize

DATASET = r"D:\Project\DATA\kitti\02"
DATASET_LEFT = DATASET+"/image_2/"
DATASET_RIGHT = DATASET+"/image_3/"
DATASET_DISPARITIES = DATASET+"/disparities/"
DATASET_COMBINED = DATASET+"/combined/"

def SGBM(left, right):
	kernel_size = 3
	smooth_left = cv2.GaussianBlur(left, (kernel_size,kernel_size), 1.5)
	smooth_right = cv2.GaussianBlur(right, (kernel_size, kernel_size), 1.5)

	window_size = 9
	left_matcher = cv2.StereoSGBM_create(
	    numDisparities=96,
	    blockSize=7,
	    P1=8*3*window_size**2,
	    P2=32*3*window_size**2,
	    disp12MaxDiff=1,
	    uniquenessRatio=16,
	    speckleRange=2,
	    mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
	)

	right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)

	wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=left_matcher)
	wls_filter.setLambda(80000)
	wls_filter.setSigmaColor(1.2)

	disparity_left = np.int16(left_matcher.compute(smooth_left, smooth_right))
	disparity_right = np.int16(right_matcher.compute(smooth_right, smooth_left) )

	wls_image = wls_filter.filter(disparity_left, smooth_left, None, disparity_right)
	wls_image = cv2.normalize(src=wls_image, dst=wls_image, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX)
	wls_image = np.uint8(wls_image)
	cv2.imshow("wls", wls_image)
	cv2.waitKey(1)

def process_dataset():
	left_images = [f for f in os.listdir(DATASET_LEFT) if not f.startswith('.')]
	right_images = [f for f in os.listdir(DATASET_RIGHT) if not f.startswith('.')]
	assert(len(left_images) == len(right_images))
	left_images.sort()
	right_images.sort()
	for i in range(len(left_images)):
		left_image_path = DATASET_LEFT+left_images[i]
		right_image_path = DATASET_RIGHT+right_images[i]
		left_image = cv2.imread(left_image_path, cv2.IMREAD_COLOR)
		right_image = cv2.imread(right_image_path, cv2.IMREAD_COLOR)
		SGBM(left_image, right_image)

if __name__== "__main__":
	process_dataset()
