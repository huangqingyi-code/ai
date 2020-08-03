#阈值：像素值高于阈值时，我们给这个像素赋予一个新值（可能是白色），否则我们给它赋予另外一种颜色（也许是黑色）
import matplotlib.pyplot as plt
import cv2
import numpy as np

# #二值化（全局）
# img = cv2.imread("image/1.jpg")
# gray = cv2.cvtColor(img,code=cv2.COLOR_BGR2GRAY)
# ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# #OTSU二值化（全局）：cv2.THRESH_OTSU  根据灰度图的双峰图自动求出灰度图的阈值
# print(ret)
# cv2.imshow("binary",binary)
# cv2.imshow("gray",gray)
# cv2.waitKey(0)

img = cv2.imread("img/5.jpg",0)
# cv2.imshow("gray",img)
# ret,threshold1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,threshold2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,threshold3 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,threshold4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret,threshold5 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# title = ["img","thresh_binary","thresh_binary_inv","thresh_tozero","thresh_tozero_inv","thresh_trunc"]
# images = [img,threshold1,threshold2,threshold3,threshold4,threshold5]
# for i in range(6):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i],"gray")
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
cv2.imshow("img",threshold5)
cv2.imshow("img1",img)
cv2.waitKey(0)

#自适应阈值（局部方法）：1.用平均的方法，则所有像素周围的权值相同。2.高斯方法,周围的像素的权值则根据其到中心点的距离通过高斯方程得到
# img = cv2.imread("image/2.jpg")
# dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,binary = cv2.threshold(dst,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# # print(ret)
# thresh_mean = cv2.adaptiveThreshold(dst,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
# thresh_gaus = cv2.adaptiveThreshold(dst,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)#2表示一个偏移值调整量，用均值和高斯计算阈值后，再减或加这个值就是最终阈值。
# title = ["original","binary","thresh_mean","thresh_gaus"]
# imges = [img,binary,thresh_mean,thresh_gaus]
# cv2.waitKey(0)
# for i in range(4):
#     plt.subplot(2,2,i+1)
#     plt.imshow(imges[i],"gray")
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()