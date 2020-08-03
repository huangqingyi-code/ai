import cv2
import numpy as np
#在图像处理中，霍夫变换用来检测任意能够用数学公式表达的形状，即使这个形状被破坏或者有点扭曲

# 霍夫变换圆检测
src = cv2.imread("image/27.jpg")
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
dst = cv2.Canny(img,100,150)
circle = cv2.HoughCircles(dst,cv2.HOUGH_GRADIENT,1,30,param1=150,param2=40,minRadius=20,maxRadius=300)
# minDist为圆心之间的最小距离，如果检测到的两个圆心之间距离小于该值，则认为它们是同一个圆心,param1为边缘检测时使用Canny算子的高阈值
# param2检测半径相等和圆心相交点重复的阈值
if not circle is None:
    for i in circle[0,:]:
        cv2.circle(src,(i[0],i[1]),i[2],(0,0,255),2)
cv2.imshow("src",src)
cv2.waitKey(0)


# 霍夫变换直线检测
# src = cv2.imread("image/16.jpg")
# img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img,(5,5),3)
# dst = cv2.Canny(img,100,150)
# lines = cv2.HoughLines(dst,1,np.pi/180,50)
# # print(lines)
# for l in lines:
#     rho,theta = l[0]
#     # x = rho*(np.cos(theta))
#     # y = rho*(np.sin(theta))
#     # print(x,y)
#     # cv2.line(src,(x,y),(x+np.tan(theta)*y,0),(0,0,255),2)
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     x1 = int(x0 + 1000 * (-b))  # 直线起点横坐标
#     y1 = int(y0 + 1000 * (a))  # 直线起点纵坐标
#     x2 = int(x0 - 1000 * (-b))  # 直线终点横坐标
#     y2 = int(y0 - 1000 * (a))  # 直线终点纵坐标 获取这条直线最小值点y2　　其中*1000是内部规则
#     cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)
# cv2.imshow("dst",src)
# cv2.waitKey(0)