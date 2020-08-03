# 作用：1.加密 2.验证
# 原理：hashlib将bytes数据类型转化成固定长度的十六进制数字组成的字符串
# 特点：1.不可逆2.相同数据转换成的结果一定相同3.MD5被王晓云破解了
# lst = [1,2,'太白']
# date = str(lst)
# print(date)
# import hashlib
# # ret = hashlib.md5()
# # ret.update(date.encode('utf-8'))
# # print(ret.hexdigest())
#
# num = str(666)
# ret = hashlib.md5('taibai'.encode('utf-8'))
# ret.update(num.encode('utf-8'))
# print(ret.hexdigest())

import hashlib
s = '中国'
s1 = '中'
s2 = '国'
ret = hashlib.md5()
ret.update(s.encode('utf-8'))
print(ret.hexdigest())
ret1 = hashlib.md5()
ret1.update(s1.encode('utf-8'))
ret1.update(s2.encode('utf-8'))
print(ret1.hexdigest())