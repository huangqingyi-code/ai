import numpy as np
import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

# x0 = torch.arange(-10.,10.)
# x0 = x0.reshape(20,1)
# x1 = torch.unsqueeze(torch.arange(-10,10),dim=1) [20,1] 20表示批次，
x0 = torch.unsqueeze(torch.arange(-10.,10.),dim=1)
y0 = x0.pow(3)
plt.scatter(x0,y0)
# plt.show()
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = torch.nn.Parameter(torch.randn(1,20))
        self.b1 = torch.nn.Parameter(torch.zeros(20))
        self.w2 = torch.nn.Parameter(torch.randn(20,64))
        self.b2 = torch.nn.Parameter(torch.rand(64))
        self.w3 = torch.nn.Parameter(torch.randn(64,20))
        self.b3 = torch.nn.Parameter(torch.rand(20))
        self.w4 = torch.nn.Parameter(torch.randn(20,1))
        self.b4 = torch.nn.Parameter(torch.rand(1))
    def forward(self,x):
        ret1 = F.relu(torch.matmul(x,self.w1)+self.b1)
        ret2 = F.relu(torch.matmul(ret1,self.w2) + self.b2)
        ret3 = F.relu(torch.matmul(ret2,self.w3) + self.b3)
        ret4 = torch.matmul(ret3,self.w4) + self.b4
        return ret4
if __name__=="__main__":
    net = Net()
    opt = torch.optim.Adam(net.parameters(),lr=0.1)
    loss_fun = torch.nn.MSELoss()
    plt.ion()
    for i in range(1000):
        out = net(x0)
        loss = loss_fun(out,y0)
        opt.zero_grad()
        loss.backward()
        opt.step()
        plt.cla()
        plt.scatter(x0,y0,c="g")
        plt.plot(x0,out.detach().numpy(),"r")
        plt.pause(0.1)
        # print(loss.item())
        print(out.reshape(20))
    plt.ioff()
    plt.show()

