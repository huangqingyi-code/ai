import cv2
import numpy as np

# Canny算法是一种边缘提取算法
# 步骤:
# 彩色图像转换为灰度图像
# 高斯滤波，滤除噪声点
# 计算图像梯度，根据梯度计算边缘幅值与角度
# 非极大值抑制
# 双阈值边缘连接处理
# 二值化图像输出结果

# src = cv2.imread("image/1.jpg")
# img = cv2.GaussianBlur(src,(5,5),1)
# img = cv2.addWeighted(src,2,img,-1,0)
# dst2 = cv2.Canny(img,50,150)
# cv2.imshow("original",src)
# cv2.imshow("dst2",dst2)
# cv2.waitKey(0)

src = cv2.imread("image/25.jpg",0)
src = cv2.convertScaleAbs(src,alpha=9,beta=1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
src = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel)
src = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel)
src = cv2.GaussianBlur(src,(3,3),1)
dst = cv2.Canny(src,130,150)
lapacian = cv2.Laplacian(src,-1)
lapacian = cv2.convertScaleAbs(lapacian,alpha=6)
ret,lapacian = cv2.threshold(lapacian,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# lapacian = cv2.medianBlur(lapacian,3)
# dst = cv2.morphologyEx(dst,cv2.MORPH_CLOSE,kernel)
cv2.imshow("lapacian",lapacian)
cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey(0)