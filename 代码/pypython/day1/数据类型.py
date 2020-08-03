# 居中，两边空白
# s = 'fasf'
# print(s.center(20,'-'))
# # 每个隔开的单词首字母大写
# s = 'ruwoij fasljg ourowieu9twf'
# print(s.title())
# 大小写翻转
# # 判断字符串以什么开头
# s = 'school'
# s1 = s.startswith('c',1)
# print(s.startswith('s'))
#
# # find index通过元素找索引，找到第一个，找不到返回-1
# print(s.find('f'))
# print(s.index('o'))
#
# # strip 删除空格 默认空格
#
# s.strip('!')  #删除！号
#
# #数数
#
# print(s.count('dd'))#字符串中dd的个数
#
# # 切片顾头不顾尾
#
# 字典
# dic = {'name':'huangqingyi','age':18}
# dic2 = {'name':'goodboy'}
# # dic.setdefault('some','boy')
# # dic.pop('some',None)
# dic2.update(dic)
# print(dic2)
#
# ==判断左右两边数值相等
# is 是指向变量的内存地址
# i1 = 4
# # i2 = 4
# # print(i1 is i2)
# id(i1) 和 id(i2)一样
# int值在-5--256  是同一个id