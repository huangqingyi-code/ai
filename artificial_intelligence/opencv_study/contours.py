import cv2
import numpy as np

# #查找轮廓
# src = cv2.imread("image/3.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# contour,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #contour是个轮廓点的列表,里面是ndarry类型
# # contour,hierarchy = cv2.findContours(src,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  #尽可能匹配多的点
# # print(hierarchy)  表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。
# print(contour)
# img_contour = cv2.drawContours(src,contour,-1,(0,0,255),2)
# print(len(contour))
# cv2.imshow("contour",img_contour)
# cv2.waitKey(0)
#
# #图像的中心/重心 通过图像的矩来求s
# M = cv2.moments(contour[0])
# x,y = int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])
# print("重心：",x,y)
#
# #area
# area = cv2.contourArea(contour[0])
# print("面积：",area)
#
# #perimeter
# perimeter = cv2.arcLength(contour[0],True)
# print("周长：",perimeter)

# 轮廓近似：将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定
src = cv2.imread("image/3.jpg")
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
perimeter = cv2.arcLength(contours[0],True)
epsilon = perimeter*0.02 #精度,越小与原图越相似
approx = cv2.approxPolyDP(contours[0],epsilon,True)
img_contour = cv2.drawContours(src,[approx],-1,(0,0,255),2)
cv2.imshow("contour",img_contour)
cv2.waitKey(0)

#凸包和凸性检测
# 函数 cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷；
# 函数 cv2.isContourConvex() 可以可以用来检测一个曲线是不是凸的。它只能返回 True 或False
#
# src = cv2.imread("image/3.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# contour,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# hull = cv2.convexHull(contour[0])
# print(cv2.isContourConvex(contour[0]),cv2.isContourConvex(hull))
# img_contour = cv2.drawContours(src,[hull],-1,(0,0,255),2)
# cv2.imshow("contour",img_contour)
# cv2.waitKey(0)

#边界检测：1.边界矩形2.最小矩形3.最小外切圆
# src = cv2.imread("image/3.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 1.边界矩形
# x,y,w,h = cv2.boundingRect(contours[0])   #返回矩形的是矩形左上角的坐标和宽/高
# img_contour = cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
# 2.最小矩形
# rect = cv2.minAreaRect(contours[0])    #返回的是矩形中心的坐标和宽/高/偏移的角度
# box = cv2.boxPoints(rect)   #转换成矩形四点的坐标
# box = np.int0(box)   #int0等于int64
# img_contour = cv2.drawContours(src,[box],-1,(0,0,255),2)
# 3.最小外切圆
# (x,y),radius = cv2.minEnclosingCircle(contours[0])
# center = (int(x),int(y))
# radius = int(radius)
# img_contour = cv2.circle(src,center,radius,(0,0,255),2)
# 4.椭圆拟合
# ellipse = cv2.fitEllipse(contours[0])
# cv2.ellipse(src,ellipse,(255,0,0),2)
# 5.直线拟合
# h,w,_ = src.shape
# [vx,vy,x,y] = cv2.fitLine(contours[0],cv2.DIST_L2,0,0.01,0.01)
# lefty = int((-x * vy / vx) + y)
# righty = int(((w - x) * vy / vx) + y)
# cv2.line(src, (w - 1, righty), (0, lefty), (0, 0, 255), 2)

# cv2.imshow("contour",src)
# cv2.waitKey(0)