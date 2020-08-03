# 增
# dic = {'name':'huangqingyi','age':18}
# dic['weight'] = 65
# dic.setdefault('age',170)  #key在dic中不添加
# print(dic)
# dic1 = dict.fromkeys('taibai',666)
# # print(dic1)
# dic1['t'] = 8
# print(dic1)

# 删
# dic = dict.fromkeys('taibai',666)
# del dic['t']
# res = dic.pop('a')
# print(dic)
# dic.clear()

# 改
# dic = {'name':'huangqingyi','age':18}
# dic.setdefault('weight',65)
# dic['age'] = 27
# dic1 = {'school':'taiyuan university','age':28}
# dic.update(dic1)
# print(dic)

# 查
# dic = {'name':'huangqingyi','age':18}
# print(dic['name'])
# print(dic.get('name',None))
# for key,value in dic.items():
#     print(f'name:{key},age:{value}')
# key = dic.keys()
# print(key)
dic = {'k1':1,"k2":2,'k3':3,'a1':10,'a2':20,'a3':30}  #在循环中可以更改key的值，不能增加或删除key
lst = []
for  i in dic.keys():
    if i.startswith('k'):
        lst.append(i)
for i in lst:
    del dic[i]
print(dic)