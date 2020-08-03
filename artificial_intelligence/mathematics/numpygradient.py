import numpy as np
# import matplotlib.pyplot as plt
# import random
#
# x1 = [x/100 for x in range(0,100)]
# y1 = [3*x+4+random.random() for x in x1]
# w = random.random()
# b = random.random()
# # print(x)
# for i in range(0,30):
#     for x,y in zip(x1,y1):
#         z = w*x +b
#         loss = (z-y)**2
#         dw = -2*x*(w*x+b-y)
#         db = -2*(w*x+b-y)
#         w = w+0.1*dw
#         b = b+0.1*db
#         print(w,b,loss)
# plt.plot(x1,y1,".")
# y = [w*x+b for x in x1]
# plt.plot(x1,y)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random
x1 = [x/100 for x in range(-100,100)]
y1 = [3*i*i+4+random.random() for i in x1]
w = random.random()
b = random.random()
plt.ion()
for i in range(0,20):
    for x,y in zip(x1,y1):
        z = w*x**2+b
        loss = (w*x*x+b-y)**2
        dw = -2*x*x*(w*x*x+b-y)
        db = -2*(w*x*x+b-y)
        w += 0.1*dw  
        b += 0.1*db
        print(f'w:{w},b:{b},loss:{loss}')
    plt.cla()
    plt.plot(x1,y1,".")
    y = [w*x*x+b for x in x1]
    plt.plot(x1,y)
    plt.pause(0.01)
plt.ioff()
plt.show()