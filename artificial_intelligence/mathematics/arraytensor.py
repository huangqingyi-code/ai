import torch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
image = Image.open("dog.jpg")
image_data = np.array(image)
# plt.imshow(image_data)   #可以用plt里面的imshow()打开
# plt.show()
print(image_data)
print(image_data.shape)


# a = np.array([1,2,3])  #(3,)是一维向量,一行三列
# b = np.array([[[1,2]],[[3,4]]])  #(2, 1, 2)三维,张量
# # print(a.shape,b.shape)
# c = torch.from_numpy(b)
# d = c.numpy()
# print(c.shape,d.shape)