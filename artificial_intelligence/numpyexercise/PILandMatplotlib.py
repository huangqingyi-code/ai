import numpy as np
from PIL import Image,ImageFilter
import matplotlib.pyplot as plt
# img = Image.open(r"image\dog.jpg")
# img.show()
# plt.imshow(img)
# plt.title("dog")
# plt.show()
# w,h = img.size
# print(w,h)
# bands = img.getbands()  #获取图片的通道("R","G","B")  opencv中通道是BGR
# print(img.mode)  #RGB
#
#
#缩放图片
# new_img = img.resize((w//2,h//2))  #整除，像素不可以小数
# img.show()
# img.thumbnail((w//2,h//2))    #缩小丢像素，放大：上采样；缩小：下采样
# img.thumbnail((w//2,h//2),rasample=Image.ANTIALIAS)  #抗锯齿
# img.show()

#抠图
# img = img.crop((100,100,350,350))
# img.show()

# #旋转
# img = img.rotate(90)
# plt.imshow(img)
# plt.show()

#滤波器
# img = img.filter(ImageFilter.BLUR)  #模糊
# img.show()
# img = img.filter(ImageFilter.DETAIL)  #细节
# img.show()
# img = img.filter(ImageFilter.CONTOUR)  #轮廓
# img.show()
# img = img.filter(ImageFilter.BoxBlur(radius=20))  #锐化
# img.show()
# img = img.filter(ImageFilter.EDGE_ENHANCE)  #edg_enhance 边缘增强
# img.show()
# img = img.filter(ImageFilter.EMBOSS)  #浮雕图案
# img.show()

#加Logo
# logo = Image.open(r"image/timg.jpg")
# logo = logo.resize((60,40),resample=Image.ANTIALIAS)
# img.paste(logo,(100,100))
# img.show()

img = Image.open(r"image\dog.jpg")
img_data = np.array(img)
# h,w,c = img_data.shape
# w,h = img.size
print(img.size)
print(img_data.shape)
img.show()
# img = img.resize((w//2,h//2))
# img.thumbnail((w//2,h//2),resample = Image.ANTIALIAS)
# print(img_data)
# img = Image.fromarray(img_data)
# img.show()