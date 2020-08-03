import torch
from torch import optim
import matplotlib.pyplot as plt
x0 = torch.arange(0,1,0.01)
y0 = 3*x0 +4+torch.rand(100)

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))
    def forward(self, x):
        return self.w * x +self.b
if __name__ == "__main__":
    line = Line()
    # opt = optim.SGD(line.parameters(),lr=0.1)
    opt = optim.Adam(line.parameters(),lr=0.1)
    plt.ion()
    for i in range(60):
        for x,y in zip(x0,y0):
            # 输出值
            z = line(x)   #会自动调用forward函数
            # 定义损失
            loss = (y-z)**2
            # 梯度清零
            opt.zero_grad()
            # 自动求导
            loss.backward()
            # 梯度更新
            opt.step()
            print(line.w.item(),line.b.item(),loss.item())
        plt.cla()
        plt.plot(x0,y0,".")
        y1 = [line.w*y+line.b for y in x0]
        plt.plot(x0,y1)
        plt.pause(0.01)

plt.ioff()
plt.show()
