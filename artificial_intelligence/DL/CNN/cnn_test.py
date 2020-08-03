import torch
from torch import nn

if __name__ == '__main__':
    conv = nn.Conv2d(3,16,kernel_size=4,stride=4,padding=1)   #pytorch默认是value模式，步长不为1，剩余的一行或一列会去掉
                                                            #tensorflow会补一列padding或者补一行padding
    x = torch.randn(1,3,5,5)
    y = conv(x)

    x = torch.tensor([[[[ 0.7504,  0.1157,  1.4940, -0.2619, -0.4732],
          [ 0.1497,  0.0805,  2.0829, -0.0925, -1.3367],
          [ 1.7471,  0.5205, -0.8532, -0.7358, -1.3931],
          [ 0.1159, -0.2376,  1.2683, -0.0959, -1.3171],
          [-0.1620, -1.8539,  0.0893, -0.0568, -0.0758]]]])
    # print(x.shape)
    m1 = torch.nn.Conv2d(1, 1, 1, padding=1)
    print(m1(x),m1.bias,m1.weight)