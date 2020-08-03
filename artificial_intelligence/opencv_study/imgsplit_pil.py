import numpy as np
from PIL import Image
import cv2

img = Image.open("img/4.jpg")
# print(type(img))  #<class 'PIL.JpegImagePlugin.JpegImageFile'>
img = np.array(img)
w,h,c = img.shape
print(img.shape)
# pic = img[225:,400:,::]
# pic = Image.fromarray(pic)
# pic.show()
img = img.reshape(2,w//2,2,h//2,c)
img = img.swapaxes(1,2)
img = img.reshape(4,w//2,h//2,c)
print(img.shape)

# img_data = np.split(img,4,axis=0)   split切割
# print(type(img_data))
# for i in img_data:
#     print(type(i))

# print(img)
# for i,pic in enumerate(img,1):
#     # print(pic.shape)
#     new_img = pic
#     new_img = Image.fromarray(new_img)
#     new_img.save(f"img{i}.jpg")

img = cv2.imread("image/1.jpg")
a,b,c = np.split(img,3,2)
new_img = cv2.merge((a,b,c))
cv2.imshow("new_img",new_img)
cv2.waitKey(0)