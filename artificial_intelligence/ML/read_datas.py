import numpy as np
import random
import matplotlib.pyplot as plt
import json

def generate_onehot():
    dic = {}
    x= np.zeros(9)
    for i in range(1,10):
        x[i-1] = 1
        dic[i] = x
        x = np.zeros(9)
    return dic
ret = generate_onehot()
# print(ret)

def class_onehot(s):
    s = list(s)
    one_index = s.index(1)
    return one_index+1
# ret = class_onehot(np.array([0,0,1,0,0]))
# print(ret)
def generate_data():
    x = [i/10 for i in range(-10,10)]
    y1 = [3*i+4+random.random() for i in x]
    z1 = [0 for i in x]
    y2 = [3*i+3-random.random() for i in x]
    z2 = [1 for i in x]
    # plt.scatter(x,y1)
    # plt.scatter(x,y2,color="r")
    # plt.show()
    with open("data/datas", mode="w", encoding="utf-8") as f:
        for a,b,c in zip(x,y1,z1):
            lst = [a,b,c]
            # f.write(f"{a} {b} {c}"+"\n")   #写入的字符串
            f.write(json.dumps(lst)+"\n")
        for a,b,c in zip(x,y2,z2):
            lst = [a, b, c]
            # f.write(f"{a} {b} {c}"+"\n")
            f.write(json.dumps(lst)+"\n")
        #  for a,b,c in zip(x,y1,z1):
        #     f.write(json.dumps(a)+"\t")
        #     f.write(json.dumps(b)+"\t")
        #     f.write(json.dumps(c)+"\n")
        #  for a, b, c in zip(x, y2, z2):
        #     f.write(json.dumps(a)+"\t")
        #     f.write(json.dumps(b)+"\t")
        #     f.write(json.dumps(c)+"\n")

generate_data()
# def reading_datas(path):
#     content = np.loadtxt(path,delimiter="\t")
#     return content
# ret = reading_datas(r"datas")
# print(ret)
# x1 = ret[ret[:,2]==0][:,:2]
# x2 = ret[ret[:,2]==1][:,:2]
# # print(x1,x2)
# plt.scatter(x1[:,0],x1[:,1],color="r")
# plt.scatter(x2[:,0],x2[:,1],color="b")
# plt.show()

# def reading_datas(path):
#     with open(path,mode="r",encoding="utf-8")as f1:
#         # ret = f1.readlines()
#         # print(ret)
#         data = []
#         for line in f1:
#             ret = json.loads(line)
#             data.append(ret)
#     return data
# res = reading_datas("datas")
# datas = np.array(res)
# x1 = datas[datas[:,2]==0]
# x2 = datas[datas[:,2]==1]
# plt.scatter(x1[:,0],x1[:,1])
# plt.scatter(x2[:,0],x2[:,1],color="r")
# plt.show()

#读取excel表格
import xlrd,tables
data = xlrd.open_workbook("data/datas.xls").sheets()[0]
rows = data.nrows
cols = data.ncols
x = np.ones((rows-1,cols))
# print(x)
# y = data.row_values(0)
# print(y)
for i in range(rows-1):
    x[i]= data.row_values(i+1)
# y = data.row_values(0)  #获取第一行所有数据 （0）为索引值

# print(x[:,2]==0)
