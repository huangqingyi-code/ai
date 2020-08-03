
# print(ord("1")) #将字符转换从ASCII码
# print(chr(90)) #将ascii码转换成字符

# l1 = [i for i in range(10)]
# l1.reverse()  #改变了原列表
# print(l1)
# obj = reversed(l1)  #生成一个迭代器
# print(list(obj))

# l1 = [1,2,4,-5,6,-40,-60,9]
# a = max(l1,key=lambda x:abs(x))
# print(a)
# dic = {"a":10,"b":2,"c":3}  #传入什么返回什么
# a = max(dic,key=lambda x:dic[x])
# print(a)

# l1 = [1,2,5,6,0,4,8,3]
# sorted(l1)
# l1.sort()
# print(l1)

l1 = [1,2,5,6,0,4,8,3]
ret = filter(lambda x:x>2,l1)  #返回的时迭代器
# res = [x for x in l1 if x>2]
# print(res)
print(list(ret))

l1 = [1,2,5,6,0,4,8,3]
ret = map(lambda x:x**2,l1)  #返回的时迭代器
print(list(ret))


