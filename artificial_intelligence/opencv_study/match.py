# 匹配模板：1.平方差匹配 CV_TM_SQDIFF/2.标准平方差匹配 CV_TM_SQDIFF_NORMED   最好匹配为0
#         3.相关匹配 CV_TM_CCORR/4.标准相关匹配 CV_TM_CCORR_NORMED         最好匹配为1
#         5.相关匹配 CV_TM_CCOEFF/6.标准相关匹配 CV_TM_CCOEFF_NORMED  1表示完美匹配,-1表示糟糕的匹配,0表示没有任何相关性
# result: 匹配结果矩阵,返回的结果是一个灰度图像，每一个像素值表示了此区域与模板的匹配程度
# minVal和maxVal: 在矩阵 result 中存储的最小值和最大值
# minLoc和maxLoc: 在结果矩阵中最小值和最大值的坐标

#单目标匹配
# import cv2
# template = cv2.imread("image/18.jpg",0)
# h,w = template.shape
# img = cv2.imread("image/9.jpg",0)
# res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
# min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
# print(min_loc,min_val)
# bottom_loc = (min_loc[0]+w,min_loc[1]+h)
# cv2.rectangle(img,min_loc,bottom_loc,(0,0,255),2)
# cv2.imshow("img",img)
# cv2.imshow("res",res)
# cv2.waitKey(0)

#多目标匹配
import cv2
import numpy as np
template = cv2.imread("image/20.jpg")
img = cv2.imread("image/19.jpg")
h,w,c = template.shape
res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
# ret = np.ravel(res)
loc = np.where(res<0.05)
for position in zip(*loc[::-1]):
    cv2.rectangle(img,position,(position[0]+w,position[1]+h),(0,0,255),1)
cv2.imshow("img",img)
cv2.waitKey(0)
# for i in range
# bottom = (min_loc[0]+w,min_loc[1]+h)
# cv2.rectangle(img,min_loc,bottom,255,2)
# cv2.imshow("img",img)
# cv2.waitKey(0)