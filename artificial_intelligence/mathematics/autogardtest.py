# 自动求导
import torch
x = torch.tensor([3.0],requires_grad=True)
y = x**2+3
y.backward()
print(x.grad)

# grd = torch.autograd.grad(y,x)
# print(grd)