# SGBM
这是使用SGBM算法实现双目测距

# 数据集
需要使用双目数据集，包含对应的左摄像头、右摄像头

# 运行
可直接运行demo.py, 数据集保存在data文件夹中

# SGBM参数说明
minDisparity	  最小可能的差异值。通常情况下，它是零，但有时整流算法可能会改变图像，所以这个参数需要作相应的调整。
numDisparities	最大差异减去最小差异。该值总是大于零。在当前的实现中，该参数必须可以被16整除。
BLOCKSIZE	      匹配的块大小。它必须是> = 1的奇数。通常情况下，它应该在3..11的范围内。
P1	            控制视差平滑度的第一个参数。见下文。
P2	            第二个参数控制视差平滑度。值越大，差异越平滑。P1是相邻像素之间的视差变化加或减1的惩罚。P2是相邻像素之间的视差变化超过1的惩罚。该算法需要P2> P1。请参见stereo_match.cpp示例，其中显示了一些相当好的P1和P2值（分别为8 * number_of_image_channels * SADWindowSize * SADWindowSize和32 * number_of_image_channels * SADWindowSize * SADWindowSize）。
disp12MaxDiff	  左右视差检查中允许的最大差异（以整数像素为单位）。将其设置为非正值以禁用检查。
preFilterCap	  预滤波图像像素的截断值。该算法首先计算每个像素的x导数，并通过[-preFilterCap，preFilterCap]间隔剪切其值。结果值传递给Birchfield-Tomasi像素成本函数。
uniquenessRatio	最佳（最小）计算成本函数值应该“赢”第二个最佳值以考虑找到的匹配正确的百分比保证金。通常，5-15范围内的值就足够了。
speckleWindowSize	平滑视差区域的最大尺寸，以考虑其噪声斑点和无效。将其设置为0可禁用斑点过滤。否则，将其设置在50-200的范围内。
speckleRange	    每个连接组件内的最大视差变化。如果你做斑点过滤，将参数设置为正值，它将被隐式乘以16.通常，1或2就足够好了。
mode	将其设置为StereoSGBM :: MODE_HH  以运行全尺寸双通道动态编程算法。它将消耗O（W * H * numDisparities）字节，这对640x480立体声很大，对于HD尺寸的图片很大。默认情况下，它被设置为false。

# 运行效果如下
![SGBM](https://user-images.githubusercontent.com/126862486/232373561-b3b249b3-a82a-4d85-98fb-4eff243d61a1.JPG)
