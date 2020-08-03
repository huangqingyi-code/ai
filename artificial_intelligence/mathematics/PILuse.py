# from PIL import Image
# import torch
# import matplotlib.pyplot as plt
# import numpy as np
# img = Image.open("dog.jpg")
# # plt.imshow(img)
# # plt.show()
# data_img = np.array(img)
# data_img = data_img.reshape(499*800*3)
# data = data_img.reshape(499,800,3)
# data = data.transpose(1,0,2)
# img = Image.fromarray(data)
# plt.imshow(img)
# plt.show()
# print(data,data.shape)

import numpy as np
from PIL import Image
import torch
img = Image.open("dog.jpg")
# img.show()
img_data = np.array(img)
# img_data = torch.from_numpy(img_data)
print(img_data.shape)
img_data = img_data.reshape(800,499,3)
# img_data = img_data.permute(1,0,2)
img = Image.fromarray(img_data)
img.show()

