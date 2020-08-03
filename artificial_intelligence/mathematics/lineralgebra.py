import torch
import numpy as np

# a = torch.tensor([[1,2],[3,4],[1,1]])
# b = torch.tensor([[5,6],[7,8],[1,1]])
# print(a+b)  #1.加减
# print(3*a)    #2.数乘/数加
# print(a*b)    #3.点乘

# a = torch.tensor([[1,2,3],[4,5,6]])
# b= torch.tensor([[1,2],[3,4],[5,6]])
# print(a@b)    #5.叉乘,M*N @ N*K =M*K   张量的叉乘只对后面两维度相乘
# print(torch.matmul(a,b))
# print(a.t())

# a = torch.tensor([[[3,2],[2,2]],[[1,1],[1,1]],[[1,0],[0,1]]])
# b = torch.tensor([[[3,2,1],[2,2,1]],[[1,1,0],[1,1,1]],[[1,0,2],[0,1,3]]])
# print(a.shape,b.shape)     #张量叉乘
# print(torch.matmul(a,b))

# x = np.array([[3,4],[1,2]])
# y = [6,5]
# res = np.matmul(x.T,y)@(np.linalg.inv(x.T@x))
# print(res)

x = torch.tensor([[1.5,0.5],[0.5,1]])
a = torch.eig(x)
b = torch.eig(x,eigenvectors=True)
# print(a)
print(b)