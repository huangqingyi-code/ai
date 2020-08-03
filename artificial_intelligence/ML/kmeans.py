import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.cluster import KMeans

data = np.random.rand(100,3)
#构建模型
estimate =KMeans(n_clusters=3)
#聚类训练
estimate.fit_predict(data)
#获取聚类中心：初始点的选择是随机的，每次聚类训练的效果都不一样
center =estimate.cluster_centers_
#获取聚类标签
label = estimate.labels_
print(center)
print(label)
# print(res)

fig = plt.figure()
axies = Axes3D(fig)
axies.scatter(data[:,0],data[:,1],data[:,2],c=label,marker="x",s=40)
axies.scatter(center[:,0],center[:,1],center[:,2],c=["r","b","g"],s=120)
plt.show()