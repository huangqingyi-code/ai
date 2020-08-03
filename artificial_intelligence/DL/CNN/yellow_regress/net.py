from torch import nn
import torch


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(in_channels=3,
                      out_channels=16,
                      kernel_size=3,
                      stride=1,
                      padding=2),



            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, 1, 2),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, 1, 2),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(64, 128, 3, 1, 2),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(128,192,3),
            nn.ReLU(),
            nn.Conv2d(192, 256, 3),
            nn.ReLU(),

        )
        self.outlayer = nn.Sequential(
            nn.Linear(256 * 16 * 16, 4)
        )

    def forward(self, x):
        h = self.layers(x)
        h = h.reshape(-1, 256 * 16 * 16)
        # print(h.shape)
        out = self.outlayer(h)
        return out


if __name__ == '__main__':
    net = Net()
    x = torch.randn(5, 3, 300, 300)
    print(net(x).shape)
