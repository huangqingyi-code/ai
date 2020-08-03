import random

# 随机小数
a = random.random()  #大于0且小于1之间的小数
b = random.uniform(1,3)  #大于1且小于3之间的小数
# print(a,b)

# 随机整数
c = random.randint(1,10)
d = random.randrange(1,10,2)   #1,10的奇数
# print(c,d)

#随机选择一个返回
# print(random.choice([1,2,["taibai"]]))

# random.seed(3)
# a = random.random()
# print(a)

#打算顺序
a = [x for x in range(10)]
print(a)
# random.seed(0)
random.shuffle(a)
# random.shuffle(a)
print(a)