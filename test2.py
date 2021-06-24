'''
    1. 同时考虑亮度偏离128的均值da和方差m
    2. 均值da越大，方差m越小，说明图片越有可能光线异常，如果均值da较小，方差m较大，说明图片光线正常
    3. 进一步地，定义：
        当da/m>1,则图片光线异常
            如果此时均值da>0, 则图片偏亮
            如果此时均值da<0, 则图片偏暗
        当da/m<1,则图片光线正常
'''

import os
import cv2
import numpy as np

def readAllPictures(pics_path):
	if not os.path.exists(pics_path):
		print("路径错误，路径不存在！")
		return
	allPics = []
	pics = os.listdir(pics_path)
	for pic in pics:
		pic_path = os.path.join(pics_path,pic)
		if os.path.isfile(pic_path):   # 只处理文件，意味着不能处理嵌套的文件夹
			allPics.append(pic_path)
			evaluate(pic_path)
	return allPics

def evaluate(image_path):
    img = cv2.imread(image_path)
    # 把图片转换为单通道的灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取形状以及长宽
    img_shape = gray_img.shape
    height, width = img_shape[0], img_shape[1]
    size = gray_img.size
    # 灰度图的直方图
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
    ma = 0
    # 计算灰度图像素点偏离均值(128)程序
    reduce_matrix = np.full((height, width), 128)   # np.full 构造一个数组，用指定值填充其元素
    shift_value = gray_img - reduce_matrix
    shift_sum = np.sum(shift_value)
    da = shift_sum / size
    # 计算偏离128的平均偏差
    for i in range(256):
        ma += (abs(i-128-da) * hist[i])
    m = abs(ma / size)
    # 亮度系数
    k = abs(da) / m
    print(image_path)
    print('亮度系数：', k)
    if k[0] > 1:
        # 过亮
        if da > 0:
            print("过亮")
        else:
            print("过暗")
    else:
        print("亮度正常")

readAllPictures('brightness/pic/all')