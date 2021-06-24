import os
import cv2
import matplotlib.pyplot as plt


# 画出图片，图片的灰度图以及图片的灰度直方图并保存
def hist(pic_path, save_path):
    plt.figure()
    # plt.figure(figsize=(20,20))
    img=cv2.imread(pic_path)    # 以彩色模式加载图片BGR
    # hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.subplot(131)
    plt.imshow(img[:,:,::-1])   # 将BGR通道翻转为RGB
    plt.xticks([])
    plt.yticks([])
    plt.subplot(132)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)		#转换为灰度图
    plt.imshow(img_gray,'gray')
    plt.xticks([])
    plt.yticks([])
    # plt.title("Original")
    plt.subplot(133)
    plt.hist(img.ravel(),256,[0,256])
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, os.path.split(pic_path)[1]))

# 获取给定目录下的所有图片的路径
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
	return allPics