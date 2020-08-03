# list1 = [0,1,2,3,4,5,6,7,8]
# del list1[1::2]  方法一
# print(list1)

# 方法二
# # list2 = []
# # for i in range(len(list1)):
# #     if i % 2 == 0:
# #         list2.append(list1[i])
# # print(list2)

# 方法三：
# for i in range(len(list1)-1,-1,-1):
#     if i % 2 ==1:
#         list1.pop(i)
# print(list1)

# l1 = []
# l2 = l1
# l3 = l1
# l3.append('a')
# print(l1,l2,l3)

# dic = {'k1':'v1','k2':'v2','a2':'av'}  #字典不允许在循环中增加、删除，可以更改值
# lst = []
# for i in dic:
#     if i.startswith('k'):
#         lst.append(i)
#         # print(lst)
# for x in lst:
#     del dic[x]
# print(dic)

# 元祖  元祖里面只有一个元素时，没有用加逗号，该是什么类型就是什么类型
# tuple1 = (9)
# tuple2 = (9,)
# print(type(tuple1),type(tuple2))

# dic1 = {'nuoshou':'sdfa'}
# dic2 = {'nuoshou':'rentougou'}
# dic1.setdefault('易大师','剑圣')
# # dic1.update(dic2)
# # del dic1['nuoshou']
# print(dic1.get('易大师','sf'))    #get查找字典中的key，没有可以自己设定返回值
# print(dic1)

# fromkeys 共用一个key
# dic = dict.fromkeys('abc',[])
# dic['a'].append(100)   #更改了一个value其他一起改变
# print(dic)


