import cv2
import numpy as np
#HSV在用于指定颜色分割时，有比较大的作用;对于不同的彩色区域，混合H与S变量，划定阈值，即可进行简单的分割。(抠图)
# img = cv2.imread("img/1.jpg")
# dst = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   #转成HSV格式后像素还是一样只是显示的模式不同，可以转回去。
#                                             # 转成灰度图转不回去，丢了像素
# new_img = cv2.cvtColor(dst,cv2.COLOR_HSV2BGR)
# print(img.shape)
# print(dst.shape)
# cv2.imshow("img",img)
# cv2.imshow("dst",dst)
# cv2.imshow("new_img",new_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread("image/11.jpg")
print(img.size)
dst = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
low_color = np.array([100,200,100])
up_color = np.array([200,255,200])
mask = cv2.inRange(dst,low_color,up_color)  #inRange()保留low-upper之间的值并改为255，其余为0
cv2.imshow("mask",mask)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()