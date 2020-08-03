import torch
from torch import nn
import math

class Net1(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.randn(784,10))
    #网络前向
    def forward(self,x):
        h = torch.matmul(x,self.w)   #w的数据类型float32  x的类型float64会报错，转成float32
        #h = x @ self.w
        h = torch.exp(h)
        z = torch.sum(h,dim=1,keepdim=True)   #keepdim加完后维度保持不变
        return h/z
class Net2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784,100)
        self.fc2 = nn.Linear(100,52)
        self.fc3 = nn.Linear(52,10)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
    def forward(self,x):
        h = self.fc1(x)
        h = self.relu(h)
        h = self.fc2(h)
        h = self.relu(h)
        h = self.fc3(h)
        out = self.softmax(h)
        return out
class Net3(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(784,100),
            nn.ReLU(),
            nn.Linear(100,52),
            nn.ReLU(),
            nn.Linear(52,10),
            nn.Softmax(dim=1)
        )
    def forward(self,x):
        return self.layer(x)
class Net4(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(784,100)*math.sqrt(2/784))   #Kaiming Initialization
        self.b1 = nn.Parameter(torch.randn(100))
        self.w2 = nn.Parameter(torch.randn(100,48)*math.sqrt(2/100))
        self.b2 = nn.Parameter(torch.randn(48))
        self.w3 = nn.Parameter(torch.randn(48,10)*math.sqrt(2/48))
        self.b3 = nn.Parameter(torch.randn(10))
    def forward(self,x):
        ret1 = nn.functional.relu(torch.matmul(x,self.w1)+self.b1)
        ret2 = nn.functional.relu(torch.matmul(ret1,self.w2)+self.b2)
        ret3 = nn.functional.softmax(torch.matmul(ret2,self.w3)+self.b3,dim=1)
        return ret3

if __name__ == '__main__':
    net = Net3()
    ret = net(torch.randn(10,784))    #先验证网络结构是否正确，每做一步确保是正确的
    print(ret.shape)
