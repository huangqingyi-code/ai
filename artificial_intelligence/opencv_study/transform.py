import cv2
import numpy as np

# img = cv2.imread("image/1.jpg")
# print(img.shape)
# cv2.imshow("img",img)
# rows,cols,channels = img.shape
# # dst = cv2.resize(img,(rows,cols),interpolation=cv2.INTER_CUBIC)   #(418, 300, 3)resize完后(300, 418, 3)
# # dst = cv2.transpose(img)  #图片转置
# dst = cv2.flip(img,-1)  #0:上下翻转  >0左右翻转  <0：上下左右翻转
# cv2.imshow("dst",dst)
# print(dst.shape)
# cv2.waitKey(0)

#仿射变换:线性变化
# import cv2
# img = cv2.imread("img/1.jpg.")
# rows,cols,channels = img.shape
# # M = np.float32([[1,0,50],[0,1,100]])
# # M = np.float32([[0.5,0,0],[0,0.5,0]])
# # M = np.float32([[-0.5,0,cols//2],[0,1,0]])
# # M = np.float32([[1,0,0],[0.5,1,0]])
# M = cv2.getRotationMatrix2D((0,0),45,1)
# dst = cv2.warpAffine(img,M,(1000,rows))
# cv2.imshow("img",img)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)

# 透视变换：不是线性变换
# src = cv2.imread("img/2.jpg")
# pst1 = np.float32([[25, 30], [179, 25], [12, 188], [189, 190]])
# pst2 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
# M = cv2.getPerspectiveTransform(pst1,pst2)
# dst = cv2.warpPerspective(src,M,(200,200))
# cv2.imshow("dst",dst)
# cv2.waitKey(0)

#膨胀操作：内核下的至少一个像素为“ 1”，则像素元素为“ 1”。因此，它会增加图像中的白色区域或增加前景对象的大小，膨胀操作前，需要二值化图像
#腐蚀操作：内核滑动通过图像(在2D卷积中)。原始图像中的一个像素(无论是1还是0)只有当内核下的所有
# 像素都是1时才被认为是1，否则它就会被侵蚀(变成0)
#腐蚀和膨胀是对白色部分（高亮部分）而言的，不是黑色部分。
# img = cv2.imread("image/3.jpg")
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# dst = cv2.dilate(img,kernel)
# dst = cv2.erode(img,kernel)
# cv2.imshow("img",img)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)

#开操作：先腐蚀后膨胀，去噪点
#闭操作：先膨胀后腐蚀，补漏洞
#梯度操作：膨胀-腐蚀，提取轮廓
#礼帽/顶帽操作：原图-开运算，获取噪音
#黑帽操作：闭运算-原图，获取漏洞
img = cv2.imread("image/4.jpg",0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# dst = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
dst = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("original",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
