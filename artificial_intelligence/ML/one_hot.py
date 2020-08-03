import numpy as np
import torch

#numpy
total_cls = 10
def onehot(cls):
    if str(cls).isdigit():
        return np.eye(total_cls)[cls]
    else:
        return np.argmax(cls)
# print(onehot(4))

#torch
x = torch.tensor([0,1,2,3,4])
# a = np.array([0,1,2,2])
# print(a.size)    #4
total_cls = 10
# print(x.size())    #torch.Size([5])
src = torch.zeros(x.size(0),total_cls)
y =  src.scatter_(1,x.reshape(-1,1),1)    #scatter_会改变原数据，scatter不会改变原数据
                                        #-1表示剩余的维度
# print(y)
# print(src)

#stack:可以将列表中ndarray的列表转成numpy.ndarray类型
x = []
x.append(np.array([1,2,3]))
x.append(np.array([4,5,6]))
# print(x,type(x))
# print(np.stack(x),type(np.stack(x)))

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
# print(np.hstack((a,b)))

max = np.argmax([[1,2,3],[4,5,6]],axis=1)#argmax有一个参数axis,默认是0,表示每一列的最大值的索引 axis=1表示每一行的最大值的索引
print(max)