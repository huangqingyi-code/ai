import numpy as np
import torch
from torch import nn

a = torch.tensor([1])
ret = torch.nn.functional.one_hot(a,4)
#a的数据类型需要整型，one_hot is only applicable to index tensor.传入模型要转回float32类型
                                          #调用nn.functional.one_hot维度从[4]变为[1,4]
ret = torch.squeeze(a)  #去掉维数为1的的维度
# print(a.shape)

x = torch.tensor([1,2,3,4,5,6])
y = x.reshape(1,2,1,3,1)
print(y.shape)
print(torch.squeeze(y).shape)