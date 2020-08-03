import numpy as np
import matplotlib.pyplot as plt
import random
import torch
x0 = [2+random.random() for i in range(30)]
y0 = [3+random.random() for i in range(30)]
x_ = [3+random.random() for i in range(30)]
y_ = [1+random.random() for i in range(30)]
x = []
y= [0 if i%2==0 else 1 for i in range(60)]
for i in range(30):
    x.append([x0[i],y0[i]])
    x.append([x_[i],y_[i]])
print(y)
plt.plot(x0,y0,".")
plt.plot(x_,y_,".")
plt.show()
w1 = random.random()
w2 = random.random()
b = random.random()
# plt.ion()
for xx,yy in zip(x,y):
    z = w1*xx[0]+w2*xx[1]+b
    loss = (z-yy)**2
    dw1 = -2*(z-yy)*xx[0]
    dw2= -2*(z-yy)*xx[1]
    db= -2*(z-yy)
    w1 += 0.01*dw1
    w2 += 0.01*dw2
    b += 0.01*db
#     print(w1,w2,b,loss)
#     plt.cla()
#     plt.plot(x0,y0,".")
#     plt.plot(x_,y_,".")
#     v = [(0.5-b-w2*x)/w1 for x in x0]
#     plt.plot(x0,v)
#     plt.pause(0.01)
# plt.ioff()
# plt.show()


