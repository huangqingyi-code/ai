import cv2
import numpy as np
import matplotlib.pyplot as plt

#滤波：把不需要的信号频率去掉，滤波操作一般用卷积操作来实现，卷积核一半称为滤波器。
# 滤波分：低通滤波，高通滤波，中通滤波，阻带滤波
# 低通滤波也叫平滑滤波，可以使图像变模糊，主要用于去噪
# 高通滤波一般用于获取图像边缘、轮廓或梯度
# 中通滤波一般用于获取已知频率范围内的信号
# 阻带滤波一般用于去掉已知频率范围内的信号
# 滤波分析一般有时域分析和频域分析
# 时域分析是直接对信号本身进行分析
# 频域分析师对型号的变化快慢进行分析
# src = cv2.imread("image/4.jpg")
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# dst = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel)
# dst1 = cv2.morphologyEx(dst,cv2.MORPH_OPEN,kernel)

# 低通滤波
src = cv2.imread("image/2.jpg")
# kernel = np.array([[1,1,0],[1,0,-1],[0,-1,-1]],dtype=np.float32)
# dst = cv2.filter2D(src,-1,kernel)
# dst = cv2.GaussianBlur(src,(3,3),5)  #高斯滤波，低通滤波，降噪，图像变模糊
# # dst = cv2.medianBlur(src,5)   #中值滤波，低通滤波，降噪，去除椒盐噪声
# # dst = cv2.blur(src,(5,5))  #均值滤波，低通滤波，降噪，图像变模糊
# dst1 = cv2.bilateralFilter(src,9,75,75)  #可以保持边缘/降噪平滑,慢
# cv2.imshow("original",src)
# cv2.imshow("dst",dst)
# cv2.imshow("dst1",dst1)
# cv2.waitKey(0)


#锐化：凸显边缘,噪点也会凸显
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  #laplacian锐化
# dst = cv2.filter2D(src,-1,kernel)

# dst = cv2.GaussianBlur(src,(5,5),1)  #USM锐化，高斯滤波，再用原图减去高斯滤波
# dst = cv2.addWeighted(src,2,dst,-1,0)
# cv2.imshow("original",src)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)

#高通滤波  laplacian滤波提取轮廓
# src = cv2.imread("image/2.jpg")
# dst = cv2.Laplacian(src,-1)
# cv2.imshow("original",src)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)
# #sobel算子
# lap = cv2.Laplacian(src,-1)
# dstx = cv2.Sobel(src,-1,1,0)   #从黑到白的边界的导数是正数，而一个从白到黑的边界点导数却是负数。如果原图像的深度是np.uint8 时，
# # 所有的负值都会被截断变成 0，换句话说就是把边界丢失掉。所以如果想同时检测到这两种边界，最好的办法就是将输出的数据类型设置得更高，
# # 比如 cv2.CV_16S， cv2.CV_64F 等。取绝对值然后再把它转回到 cv2.CV_8U。
# dstx = cv2.convertScaleAbs(dstx)
# dsty = cv2.Sobel(src,-1,0,1)
# dsty = cv2.convertScaleAbs(dsty)
# dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
# tile = ["lap","dstx","dsty","dst"]
# pic = [lap,dstx,dsty,dst]
# for i in range(4):
#     plt.subplot(2,2,i+1)
#     plt.imshow(pic[i],"gray")
#     plt.title(tile[i])
#     plt.xticks([],plt.yticks([]))
# plt.show()
# # cv2.imshow("dsty",dsty)
# # cv2.imshow("dstx",dstx)
# # cv2.imshow("dst",dst)
# # cv2.waitKey(0)




