import cv2,torch
from MINIST.net import Net1
import numpy as np
from torchvision import transforms

img = cv2.imread("6.jpg",0)
img = cv2.resize(img,(28,28))
# cv2.imshow("img",img)
# cv2.waitKey(0)
img = img.reshape(1,1,28,28)
img = img.astype(np.float32)
img = torch.from_numpy(img)

# print(img.shape)
net = Net1()
net.load_state_dict(torch.load("MINIST/checkpoint/7.t"))
res = net(img)
print(torch.argmax(res).item())
print(res)