import matplotlib.pyplot as plt
import torch
import numpy as np
from sklearn import preprocessing

x = torch.randn(100,2)
# scaler = preprocessing.StandardScaler()
# x = scaler.fit_transform(x)
# scaler = preprocessing.Normalizer(norm="l2")
# x = scaler.fit_transform(x)
# print(x[:,0])
# x0 = x[:,0]
# y0 = -torch.exp(1/2*x0**2)/(torch.sqrt(torch.tensor(2*3.1415926)))
plt.hist(x[:,0],bins=30)
plt.show()
# plt.hist(x = x[:,0], # 指定绘图数据
#         bins = 50, # 指定直方图中条块的个数
#         color = 'steelblue', # 指定直方图的填充色
#         edgecolor = 'black' # 指定直方图的边框色
#        )
# 添加x轴和y轴标签
# plt.xlabel('data')
# plt.ylabel('freq')
# 添加标题
# plt.title('gassuian')