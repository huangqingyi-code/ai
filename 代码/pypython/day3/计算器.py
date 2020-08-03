import re
exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = re.sub('( )*','',exp)
# 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# res = re.findall('\([^()]+\)',ret)
res = re.sub('\([^()]+\)','1',ret)
def remove_braket(element):
    res = re.split('([+/*])',element)
    exp = res
    return exp
ret = remove_braket('-40/5')
print(ret,type(ret))
print(4/5)
# 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))

# exp1 = '9-25/3+7/399/42998+10568/14'
# res = re.findall('\d+[/*]\d+(?:[/*]\d+)*',exp1)
# print(res)

# s1 = '<a>wahaha</a><b>banana</b><h1>qqxing</h1>'
# # 这样的字符串中，
# # 1）匹配出wahaha，banana，qqxing内容。
# # 2）匹配出a,b,h1这样的内容
# ret = re.findall('<\w+>(.*?)</\w+>',s1)
# ret1 = re.finditer('<(?P<name>\w+)>.*?</(?P=name)>',s1)
# lst = [i.group('name') for i in ret1]
# print(lst)

# 9、1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式
# s = '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))'
# ret = re.findall('\([^()]+\)',s)
# print(ret)