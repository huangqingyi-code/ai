from torch import nn
import torch


class Net1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, 1, 1),
            nn.MaxPool2d(2),
            nn.ReLU(),
            nn.Conv2d(16, 32, 1, 1),
            nn.MaxPool2d(2),
            nn.ReLU(),
            nn.Conv2d(32, 64, 1, 1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 1, 1),
            nn.ReLU(),
            nn.Conv2d(128, 256, 1, 1),
            nn.ReLU()
        )
        self.out_layer = nn.Sequential(
            nn.Linear(256 * 25 * 25, 2),
            nn.Softmax(dim=-1)
        )
        self.params = list(self.out_layer.named_parameters())
        self.param2 = list(self.layers.named_parameters())

    def forward(self, x):
        h = self.layers(x)
        # print(h.shape)
        self.h = h.reshape(-1, 256 * 25 * 25)
        out = self.out_layer(self.h)
        return out


if __name__ == '__main__':
    net = Net1()
    x = torch.randn(6, 3, 100, 100)
    y = net(x)



    print(y.shape)
    print(net.h.shape)
    # print(net.params)
