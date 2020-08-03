# # numpy是一种开源的数值计算扩展，底层是c写的
# #numpy的主要对象是同种元素的多维数组；在numpy中维度（dimensions）叫做轴（axes）；
# #matrix是array的分支，二维的array的是矩阵，
import numpy as np
import torch
# a = np.array([1,2,3]) #'numpy.ndarray'
# b = [4,5,6] #'list'
# d = np.array(b)  #用列表构造np.array
# c = torch.tensor([1,2,3]) #'torch.Tensor'
# print(a.dtype)  #a里面数据的类型int32
# print(type(a))
# print(type(b))
# print(c.dtype)  #torch.int64
# print(type(c))
# print(a.shape)
# print(a.ndim)  #维度
# print(a.size)  #个数
#
# print("zeros/ones/empty")
# a = np.zeros((2,3),dtype=np.int32) #可以更改dtype的数据类型
# b = np.ones((3,2))
# c = np.empty((3,3))  #生成随机数的数组
# print(a)
# print(a.dtype)
# print(b)
# print(b.dtype)
# print(c)
#
# print("使用arrange生成连续的元素")
# a = np.arange(-10,10,0.5)
# b = np.arange(-10,10).reshape(4,5)
# print(a)
# print(b)
#
# print("使用astype复制数组，并改变元素类型")
# a = np.array([1,2,3,4,5,6],dtype=np.float32)
# b = a.astype(np.int32)
# print(a.dtype)
# print(b,b.dtype)
#
# print("将字符串类型的元素转为数值元素")
# a = np.array(["1","2","3"])
# b = a.astype(np.int32)
# print(a.dtype)
# print(b.dtype)
#
# print("使用其他数组元素的数据类型作为参数")
# a = np.array([1,2,3],dtype=np.int32)
# b = np.array([4,5,6],dtype=np.float64)
# print(b)
# print(b.astype(a.dtype))
# print(a.dtype)
#
# print("ndarray的运算")
# a = np.array([1,2,3])
# print(a*3)  #点乘
# print(a>2)  #掩码，>2为true
# print(a*[4,5,6]) #数乘
#
# print("ndarray的基本索引")  #索引会降维
# a = np.array([[1,2],[3,4],[5,6]])
# print(a[0][1])
# print(a[0,1])  #,表示下一个维度
# b = np.array([[[[[1]]],[[[2]]],[[[3]]]],[[[[2]]],[[[1]]],[[[1]]]],[[[[3]]],[[[2]]],[[[2]]]],[[[[4]]],[[[5]]],[[[5]]]],[[[[5]]],[[[1]]],[[[1]]]]])
# print(b.shape)
#
# a = np.array([[1,2],[3,4]])
# b = a.copy()  #复制一个数组
# a[0,0]=0
# print(a)
# print(b)
#
# print("ndarray的切片")  #切片不会降维,顾头不顾尾
# a = np.array([[[1,2],[5,6]],[[3,4],[7,8]]])
# print(a.shape)
# print(a[:2,:1])
#
# print("ndarray的bool索引")
a = np.array([1,2,3,4,5])
b = np.array([True,False,True,True,True])
# b = [True,False,True,True,True]
# print(a[b])
# print(a[b==False])
# print(a[a>2])
# c = a>3
# print(c)
#
# print("ndarray的数组索引")
# a = np.array([[1,2],[3,4]])
# print(a[[0,1],0])
# print(a[[0,1]][:1,0])
#
# print("ndarray的轴")
# a = np.arange(8).reshape(4,2)
# print(np.matmul(a,a.T))  #矩阵乘法，matmul() and dot()都可以
# print(np.dot(a,a.T))  #a.T矩阵转置
# #axes transpose
# a = np.arange(24).reshape(3,2,4)
# print(a.transpose(1,0,2).shape)  #shape2，3，4
# a = a.swapaxes(0,2) #swapaxes交换指定的两个轴
# print(a.shape)
#
# print("numpy的基本统计")
# a = np.array([[1,2],[3,4],[5,6]])
# print(a .mean(axis=-1))
# print(a.sum())
# print(a.sum(axis=0))
# print(a.max(axis=1))
#
# print("where函数")
# a = np.array([1,2,3,4,5,6])
# b = np.where(a>2,1,0)
#只有条件 (condition)，没有x和y，以tuple的形式给出元素的坐标，原数组有多少维，输出的tuple中就包含几个数组
# print(np.where(a>3))  (array([1, 2, 2], dtype=int64), array([1, 0, 1], dtype=int64))
# a = np.array([[1,2],[3,4],[5,6]])
# print(a[a>3])
# print(np.where(a>3))
# print(b)
#
# print("ndarray的存取")
# a = np.array([[1,2,3],[4,5,6]])
# np.save("file",a)
# ret = np.load("file.npy")
# print(ret)
#
# print("矩阵求逆")
# a = np.array([[1,2],[3,4]])
# b = np.linalg.inv(a)
# print(b)
#
# print("numpy中随机数")
# a = np.random.randint(0,2,10000)
# print((a>0).sum())
#
# #numpy中广播
# #数组运算时shape不一样时会使用广播机制，调整数组的形状，使得shape一样，满足规则，则可以运算，否则会报错

#stack
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# # print(a)
# c = np.hstack((a,b))
# # d = np.vstack((a,b))
# print(c)
# # print(d)
#
#ravel转成一维
# x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# y = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])
# print(np.hstack((x,y)))  #要有相同的形状

# a = np.array([[1,2,3],[4,5,6]])
# b = np.where(a>2)
# print(b)
# print(a[a>2])