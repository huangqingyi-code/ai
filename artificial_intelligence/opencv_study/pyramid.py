import cv2
import numpy as np

#下采样，长宽各缩短一半
# img = cv2.imread("image/12.jpg")
# for i in range(3):
#     cv2.imshow(f"{i+1}",img)
#     img = cv2.pyrDown(img)
# cv2.waitKey(0)

#上采样，长宽各增加一倍
# img = cv2.imread("image/13.jpg")
# for i in range(3):
#     cv2.imshow(f"{i+1}",img)
#     print(img.shape)
#     img = cv2.pyrUp(img)
# cv2.waitKey(0)

#laplacian pyramid:拉普拉斯金字塔由高斯金字塔计算得来,表示轮廓
# img = cv2.imread("image/12.jpg")
# for i in range(2):
#     print(img.shape)
#     down_img = cv2.pyrDown(img)
#     up_img = cv2.pyrUp(down_img)
#     print(up_img.shape)     #700/2/2/2=87.5报错
#     laplacian = cv2.subtract(img,up_img)
#     laplacian = cv2.convertScaleAbs(laplacian,alpha=5)
#     img = down_img
#     cv2.imshow(f"{i+1}",laplacian)
# cv2.waitKey()

#无缝融合
img1 = cv2.imread("image/21.jpg")
img2 = cv2.imread("image/22.jpg")
# print(img1.shape,img2.shape)
a = img1.copy()
gaua = [a]
for i in range(5):
    a = cv2.pyrDown(a)
    gaua.append(a)
b = img2.copy()
gaub = [b]
for i in range(5):
    b = cv2.pyrDown(b)
    gaub.append(b)
lpa = [gaua[5]]
for i in range(5,0,-1):
    new = cv2.pyrUp(gaua[i])
    l = cv2.subtract(gaua[i-1],new)
    lpa.append(l)
lpb = [gaub[5]]
for i in range(5,0,-1):
    new = cv2.pyrUp(gaub[i])
    l = cv2.subtract(gaub[i-1],new)
    lpb.append(l)
lap = []
for la,lb in zip(lpa,lpb):
    h,w,c = la.shape
    ls = np.hstack((la[:,0:w//2],lb[:,w//2:]))
    # ls = cv2.convertScaleAbs(ls,alpha=20)
    # print(ls.shape)
    # cv2.imshow("ls",ls)
    # cv2.waitKey(0)
    lap.append(ls)
pic = lap[0]
for i in range(1,6):
    img = cv2.pyrUp(pic)
    pic = cv2.add(img,lap[i])
    # cv2.imshow(f"{i}",pic)

real = np.hstack((img1[:,0:w//2],img2[:,w//2:]))
cv2.imshow("real",real)
cv2.imshow("pic",pic)
cv2.waitKey(0)