import torch,numpy,cv2
from net import Net1
from torchvision import transforms

net = Net1()
net.load_state_dict(torch.load("checkpoints/3.t"))
# x = torch.randn(1,3,100,100)
# y = net(x)
# print(y)

x1 = cv2.imread("1.5990.jpeg")
x2 = cv2.imread("0.3.jpeg")
decode = transforms.ToTensor()
x1 = decode(x1).reshape(1,3,100,100)
x2 = decode(x2).reshape(1,3,100,100)
y1 = net(x1)
y2 = net(x2)
print(y1,y2)

print(net.params[0][1])
print(torch.sum(net.params[0][1],-1))


# print(torch.sum(net.params[0][1],dim=-1))

# x = (net.params[0][1][0]-net.params[0][1][1]).reshape(1,-1)
# y = net.h.t()
# print(x@y)
# print(len(net.params[0][1][0]))

# print(net.params.__len__())
# x = torch.randn(6,3,100,100)
# y = net(x)
# print(y)

# a = net.params[0][1][0].detach()
# b = net.params[0][1][1].detach()
# a = a.numpy()
# a = list(a)
# alist = sorted(a,key=lambda x:abs(x))
# alist = torch.tensor(alist)
#
# b = b.numpy()
# b = list(b)
# blist = sorted(b,key=lambda x:abs(x))
# blist = torch.tensor(blist)
# print(alist)
# print(blist)