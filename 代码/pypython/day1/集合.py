# 集合：可变的数据类型，他里面必须是不可变的数据类型，无序，去重
# 增
# set1 = {1,2,3,4}
# # set1.add(5)
# set1.update('132')
# print(set1)

# 删
set1 = {1,2,3,4}
# set1.pop() #有返回值，随机删除
set1.remove(1)
# set1.clear()
# del set1
# print(set1)

a=dict.fromkeys('abd',12)
print(a)