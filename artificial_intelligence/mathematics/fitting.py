import torch
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
img = Image.open("dog.jpg")
img_data = np.array(img)
# print(img_data,img_data.shape)
# plt.imshow(img)
# plt.show()
torch_data = torch.from_numpy(img_data)
torch_data = torch_data.permute(0,1,2)
torch_data.t()
