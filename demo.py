import os
import cv2
import numpy as np
from SGBM import SGBM


def run():
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
		img = SGBM(left_image, right_image)
		cv2.imshow("wls", img)
		cv2.waitKey(0)


DATASET = r"data\kitti\02"   # 设置数据集路径
DATASET_LEFT = DATASET+"/image_2/"		# 设置左摄像头图像路径
DATASET_RIGHT = DATASET+"/image_3/"		# 设置右摄像头图像路径

if __name__== "__main__":
	run()
	print("finished")