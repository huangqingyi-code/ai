from torch import nn
import torch

class Net1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1,16,3,1,1),
            nn.MaxPool2d(2),
            nn.ReLU(),
            nn.Conv2d(16,32,1,1),
            nn.MaxPool2d(2),
            nn.ReLU(),
            nn.Conv2d(32,64,1,1),
            nn.ReLU()
        )
        self.out_layer = nn.Sequential(
            nn.Linear(64*7*7,10),
            nn.Softmax(dim=-1)
        )
    def forward(self,x):
        h = self.layers(x)
        h = h.reshape(-1,64*7*7)
        # print(h.shape)
        out = self.out_layer(h)
        return out

if __name__ == '__main__':
    net = Net1()
    x = torch.randn(6,1,28,28)
    y = net(x)
    print(y.shape)