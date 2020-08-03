import torch
import numpy as np
import random
import matplotlib.pyplot as plt

# x1 = torch.arange(-1,1,0.1).reshape(20,1)
# x2 = 3*x1
# x = torch.stack((x1,x2))
# print(x)

x1 = np.arange(-1,1,0.1).reshape(20,1)
x2 = 3*x1+2+np.random.rand(20)
print(x2.shape)
# plt.scatter(x1,x2)
# plt.show()
