# 序列化模块：将一种数据类型（list、tuple、dic...）转化成特殊序列
# 为什么存在序列化？
# 数据----->bytes
# 只有字符串类型可以和bytes转化
# dict，list，tuple------>str<----->bytes
# 数据存储在文件中，str（bytes类型）形式存储，比如字典
# 数据通过网络传输（bytes），str不能还原回去
# 特殊的字符串：序列化
# json是一种所有的语言都可以识别的数据结构
# pickle只针对python
# dumps 和 loads一般用于网络传输，但也可以读写文件
import json
# dic = {'name':'太白','password':123}
# str = json.dumps(dic)
# print(str,type(str))
#
# dic1 = json.loads(str)
# print(dic1,type(dic1))


# dic1 = {'name':'alex'}
# dic2 = {'name':'maple'}
# dic3 = {'name':'petter'}
# with open('json文件',encoding='utf-8',mode='w') as f1:
#     f1.write(json.dumps(dic1)+'\n')
#     f1.write(json.dumps(dic2)+'\n')
#     f1.write(json.dumps(dic3)+'\n')
# with open('json文件',encoding='utf-8',mode='r')as f2:
#     for i in f2:
#         print(json.loads(i))
# dump load只能写入文件，只能写入一个数据结构

import pickle
# # dumps loads只能用于网络传输，不能写入文件
# # dump load 可以一次写入多个数据
dic1 = {'name':'alex'}
dic2 = {'name':'maple'}
dic3 = {'name':'petter'}
# with open('pickle_file',mode='wb') as f1:
#     pickle.dump(dic1,f1)
#     pickle.dump(dic2, f1)
#     pickle.dump(dic3, f1)
with open('pickle_file',mode='rb')as f2:
    for i in f2:
        print(pickle.load(i))
    # res = pickle.load(f2)
    # print(res)
    # print(pickle.load(f2))
    # print(pickle.load(f2))