import argparse
import cv2,numpy
import matplotlib.pyplot as plt

# # 设置参数
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# 	help = "Path to the image to be scanned")
# args = vars(ap.parse_args())
# # 读取输入
# image = cv2.imread(args["image"])
# #坐标也会相同变化
# ratio = image.shape[0] / 500.0
# orig = image.copy()
# image = cv2.resize(orig, height = 500)

img = cv2.imread(r"D:\pycharm\pycharm project\artificial_intelligence\opencv_study\img\page.jpg")
h,w,c = img.shape
print(img.shape)
ratio = 500/h
scale_percent = ratio # percent of original size
width = int(img.shape[1] * scale_percent)
height = int(img.shape[0] * scale_percent)
dim = (width, height)
img2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print(img2.shape)
cv2.imshow("img",img2)
cv2.waitKey(0)
