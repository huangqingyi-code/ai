import numpy as np
import matplotlib.pyplot as plt
# x = np.arange(-100,100)
# y = x ** 3
# plt.plot(x,y)
# plt.show()
#
# import torch
# import numpy as np
# a = torch.tensor(1)
# b = a.numpy()
# import numpy as np
import torch
# import matplotlib.pyplot as plt
# x = np.arange(0.1,10,0.1)
# y0 = np.zeros_like(x)
# y = np.log(x)/(np.log(np.array([0.5])))
# plt.plot(x,y0)
# plt.plot(x,y)
# plt.show()
# x = np.arange(-10,10,0.1)
# tanh = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
# y = (1+np.exp(-x))**(-1)
# plt.plot(x,tanh)
# plt.plot(x,y)
# plt.show()
# x = np.arange(-10,10,0.1)
# y = [0.5*x if x <0 else x for x in x]
# y0 = np.tile(np.array([0]),x.shape)
# plt.plot(x,y)
# plt.plot(x,y0)
# plt.show()
# a = np.array(1)
# b= torch.tensor(1)
# c = torch.from_numpy(a)
# c = b.numpy()
# print(a,type(a),b,type(b))

# x = np.arange(0,20)
# y = np.tile(np.array([3]),x.shape)
# plt.plot(x,y)
# plt.show()

x = np.zeros(40)
y = np.arange(-20,20)
x1 = np.arange(-20,20)
# y1 = np.zeros_like(x1)
y1 = np.tile(0,x.shape)
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()