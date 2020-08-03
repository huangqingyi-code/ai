import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import random
m = torch.range(-16,16,0.2)
n = torch.range(0,100,0.2)
date = []
for a in m:
    for b in n:
        date.append([a,b])
x0 = np.arange(-10.,10.)
y0 = x0**2
y1 = y0+20*random.random()
y2 = y0-10*random.random()
# plt.plot(x0,y0)
# plt.scatter(x0,y1)
# plt.scatter(x0,y2)
# plt.show()
x = []
for i in range(len(x0)):
    x.append([x0[i],y1[i]])
    x.append([x0[i],y2[i]])
y = [1 if i%2==0 else 0 for i in range(40)]
x = torch.tensor(x)
y = torch.tensor(y).reshape(40,1)
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = torch.nn.Parameter(torch.randn(2,12))
        self.b1 = torch.nn.Parameter(torch.zeros(12))
        self.w2 = torch.nn.Parameter(torch.randn(12,24))
        self.b2 = torch.nn.Parameter(torch.zeros(24))
        self.w3 = torch.nn.Parameter(torch.randn(24, 1))
        self.b3 = torch.nn.Parameter(torch.zeros(1))

    def forward(self,x):
        ret1 = F.tanh(torch.matmul(x,self.w1)+self.b1)
        ret2 = F.tanh(torch.matmul(ret1,self.w2)+self.b2)
        ret3 = F.sigmoid(torch.matmul(ret2,self.w3)+self.b3)
        return ret3
if __name__=="__main__":
    net = Net()
    opt = torch.optim.Adam(net.parameters())
    loss_func = torch.nn.MSELoss()
    for j in range(100):
        for i in range(100):
            out = net(x)
            loss = loss_func(out,y.float())
            opt.zero_grad()
            loss.backward()
            opt.step()
            # print(loss.item())
        # date = []
        # for m in range(-16,16):
        #     for n in range(0,120,4):
        #         date.append([m,n])
        date = torch.tensor(date).float()
        # print(date.shape)
        res = net.forward(date)
        res = res[:,0]
        # print(res.shape)
        res = res.numpy()
        res2 = res.copy()
    #     big = []
    #     small = []
    #     res = [i.item() for i in res]
    #     for i in range(len(res)):
    #         if res[i]>0.5:
    #             big.append(date[i])
    #         else:
    #             small.append(date[i])
    #     x1 = [i[0].item() for i in big]
    #     y1 = [i[1].item() for i in big]
    #     x2  = [i[0].item() for i in small]
    #     y2 = [i[1].item() for i in small]
    #     plt.clf()
    #     plt.scatter(x1,y1,c="r")
    #     plt.scatter(x2,y2)
    #     plt.pause(0.1)
    #     # plt.show()
    # plt.ioff()
    # plt.show()