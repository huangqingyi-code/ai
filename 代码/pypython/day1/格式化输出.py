# 格式化输出
# % s d
# name = input('请输入姓名')
# age = input('请输入年龄')
# message = '我叫%s,今年%s岁,学习进度3%%' % (name, age)
# 3%%转义表示3%
# print(message)
# a = '我是{},名字{}，年龄{}'.format('黄清仪','黄清仪','27')
# b = '我是{0},名字{0}，年龄{1}'.format('黄清仪','27')
# name ='hqy'
# age = 27
# c= '我是{name},名字{name}，年龄{age}'.format(name = name, age = age)
# print(a,b,c)
name = 'huangqingyi'
age = '27'
msg = f'我是{name},年龄{age}'
print(msg)

