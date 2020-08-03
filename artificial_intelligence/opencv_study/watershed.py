import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("image/27.jpg")
img = cv2.GaussianBlur(src,(3,3),1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 距离变换的定义是计算一个图像中非零像素点到最近的零像素点的距离,再通过二值化找到该图像的几何中心
#CV_DIST_C、CV_DIST_L1、CV_DIST_L2（maskSize=5）的计算结果是精确的，CV_DIST_L2（maskSize=3）是一个快速计算方法。
dist_transform = cv2.distanceTransform(opening,2,5)   #计算图像中每一个非零点距离离自己最近的零点的距离
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# Marker labelling:现在知道了那些是背景那些是硬币了。那我们就可以创建标签（一个与原图像大小相同，数据类型为 in32 的数组），
# 并标记其中的区域了,对我们不确定的区域使用0标记
ret, markers1 = cv2.connectedComponents(sure_fg)
# 确保背景是1不是0
markers = markers1 + 1
# 未知区域标记为0
markers[unknown == 255] = 0
#实施分水岭算法：标签图像将会被修改，边界区域的标记将变为 -1
markers3 = cv2.watershed(src, markers)
src[markers3 == -1] = [0, 0, 255]

print(markers1.shape)
cv2.imshow("img",src)
cv2.waitKey(0)