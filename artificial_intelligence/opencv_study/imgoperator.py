import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#加减法
# x = np.uint8([100])
# y = np.uint8([120])
# print(cv2.add(x,y))   #add()针对uint类型的数据，最大不能超过255，最小不能小于0
# print(cv2.subtract(x,y))

#混合
# img1 = cv2.imread("image/1.jpg")
# img2 = cv2.imread("image/6.jpg")
# dst = cv2.addWeighted(img1,0.7,img2,0.3,0)  #图像的混合：两幅图像的权重不同，这就会给人一种混合或者透明的感觉
# # dst = img1+img2   #这种是numpy中的加法，250+10 = 260 % 256 = 4
# # dst = cv2.add(img1,img2)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#按位运算（掩膜结合）： AND， OR， NOT， XOR 等。当我们提取图像的一部分，选择非矩形 ROI(region of interest) 时这些操作会很有用 。
#将一个logo覆盖到另一个图片上
logo = Image.open("image/6.jpg")
logo = logo.crop((0,150,300,250))
logo.save("logo.jpg")
logo = cv2.imread("logo.jpg")
print(logo.shape)
# logo = logo[...,::-1]
rows,cols,channels = logo.shape
logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(logo_gray,127,255,cv2.THRESH_BINARY)   #黑底白字
img = cv2.imread("image/1.jpg")
# img = img[...,::-1]
roi = img[0:rows,0:cols]
mask_inv = cv2.bitwise_not(mask)  #白底黑字（前景0，背景255）
img_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg = cv2.bitwise_and(logo,logo,mask=mask)# 就是 2个数据都要先和mask按位和 然后再按位和 如果有mask这个参数的话
# 通过位的与运算，达到“掩盖”的目的
# cv2.imshow("img",img)
dst = cv2.add(img_bg,img_fg)
img[0:rows,0:cols] = dst
# img = img[...,::-1]
cv2.imshow("img",img)
cv2.waitKey(0)