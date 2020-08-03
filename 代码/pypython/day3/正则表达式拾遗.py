# 分组命名
# (?P<name>正则表达式)
# ret.group('name')
import re
# ret = re.search('\d(?P<name>\w+)(\n?)','2323fsdfgrfs434   ')
# print(ret.group('name'))
# ret1 = re.findall('12(?:\d){2}(nsf)*','1233nsfnsf')   #?:不去组里面的元素
# print(ret1)
# 分组命名的引用

s1 = '<abc>fsadfsfsfsf</abc>fsrwerwf</abd>'
ret2 = re.search('<(?P<name>\w+)>.*?</(?P=name)>',s1)
print(ret2.group('name'))

# 转义字符在python里和正则表达式里意义不同，在正则表达式中字符串前面几r'ffsf\n',
# # 只表示正则表达式中的意义