import torch
from torch import nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(10000,1200),
            nn.ReLU(),
            nn.Linear(1200,800),
            nn.ReLU(),
            nn.Linear(800,600),
            nn.ReLU(),
            nn.Linear(600,480),
            nn.ReLU(),
            nn.Linear(480,200),
            nn.ReLU(),
            nn.Linear(200,48),
            nn.ReLU(),
            nn.Linear(48,1),
            nn.Sigmoid()
        )
    def forward(self,x):
        return self.layer(x)
if __name__ == '__main__':
    net = Net()
    x = torch.randn(5,10000)
    print(net(x).shape)