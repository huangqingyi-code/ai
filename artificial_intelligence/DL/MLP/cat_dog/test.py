import torch,numpy

y = torch.tensor([[2.],[2],[1],[0],[1]])
# y = y.numpy()
# y = numpy.where(y>=0.5,1,0)

test_tag = torch.tensor([0., 1, 1, 0, 1])

res = (y.reshape(-1)-test_tag)**2
print(res)
print(torch.mean(res))