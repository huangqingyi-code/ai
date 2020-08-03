# json 不同语言都遵循的一种数转换格式，但python中并不是所有的数据类型都支持。json序列化只支持部分Python数据结构：dict,list, tuple,str,int, float,True,False,None
# pickle ： 只支持python语言，内部所有的数据结构都支持
# pickle用于网络传输：dumps、loads    dumps里面写具体数据，dump里面写文件句柄格式
#       用于文件写读：dump、load      loads里面写具体数据，load里面写文件句柄格式
# 将list/dict等数据类型转换成特殊的字符串在类型，才可以存储和网络传输（str的类型）---序列化
import json
lst1 = [1,2,3,'太白']
lst2 = [4,5,6,'太白']
lst3 = [7,8,9,'太白']
# def fun():
#     print(666)
# # with open('jsonfile',mode='w',encoding='utf-8')as f:
# #     f.write(json.dumps(lst))
# with open('jsonfile',mode='w')as f1:
#     f1.write(json.dumps(lst1)+'\n')
#     f1.write(json.dumps(lst2)+'\n')
#     f1.write(json.dumps(lst3)+'\n')
# with open('jsonfile',mode='r',encoding='utf-8')as f2:
#     for line in f2:
#         print(json.loads(line))
import pickle
# with open('序列化',mode='wb')as f:
#     pickle.dump(lst1,f)
#     pickle.dump(lst2, f)
#     pickle.dump(lst3, f)
# with open('序列化',mode='rb')as f1:
#     print(pickle.load(f1))
#     print(pickle.load(f1))
#     print(pickle.load(f1))
with open('jsonfile', mode='w', encoding='utf-8')as f:
    f.write(str(lst1))
    # f.write(json.dumps(lst1)+"\n")
    # f.write(json.dumps(lst2)+"\n")
    # f.write(json.dumps(lst3)+"\n")
# with open('jsonfile',mode='r',encoding='utf-8')as f1:
    # cont = list(f1)
    # print(cont)
#     conten = f1.readlines()
#     contet = json.loads(conten)
#     print(contet)
