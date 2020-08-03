# name = input('请输入用户名')
# pass_word = input('请输入密码')
# message = '{}\t{}'.format(name,pass_word)
# print(message)
cars = ['鲁A534','鲁B534','黑B787','闽D8888']
locals = {'鲁':'山东','黑':'黑龙江','闽':'福建'}
lst1 = []
for i in range(len(cars)):
    lst1.append(cars[i][0])
lst2 = []
for i in lst1:
    lst2.append(locals[i])
result = {}
for i in lst2:
    if i in result:
        result[i] +=1
    else:
        result.setdefault(i,1)
print(result.get('山'))
print(result)
