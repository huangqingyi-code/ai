# info = input('>>>>>')
# for i in info:
#     if i.isalpha():
#         info = info.replace(i,' ')
# l = info.split()
# print(len(l))

# dic = {'name':'huangqingyi','age':18}
# # dic.setdefault('some','boy')
# # dic.pop('some',None)
# print(bool(dic.get('weight')))
# print(dic)

li = [{'name':'apple','price':5},{'name':'banana','price':2},{'name':'orange','price':5},
{'name':'pear','price':5}
      ]
shopping_car = {}
print('welcome to fruit store')
for num,i in enumerate(li,1):
    print('序号:{} 品种：{} 单价：{}'.format(num,i['name'],i['price']))
money = input('please input your budget for fruit')
tol_money = 0
while True:
    if money.isdigit():
        sequence = input('请选择您所需要水果的序号！')
        num = input('您要购买商品的数量')
        if sequence.isdigit() and (int(sequence) in [x for x in range (1,len(li)+1)]):
            tol_money += li[int(sequence)-1]['price'] * int(num)
            if li[int(sequence)-1]['name'] in shopping_car:
                shopping_car[li[int(sequence) - 1]['name']] += int(num)
            else:
                shopping_car[li[int(sequence) - 1]['name']] = int(num)
                print(shopping_car)
                if tol_money <= int(money):
                    print('是否还需要购买，如果需要请输入1，输入其他结束购买')
                    message = input('<<<<<')
                    if int(message) == 1:
                        pass
                    else:break
                else:
                    print('余额不足请删除一下商品')
                    while True:
                        del_sequence = input('请输入删除的序号')
                        del_num = input('请输入删除的数量')
                        if int(del_num) > shopping_car[li[int(sequence) - 1]['name']]:
                            shopping_car.pop(li[int(sequence) - 1]['name'])
                        else:
                            shopping_car[li[int(sequence) - 1]['name']] -= int(del_num)
                            tol_money -= li[int(sequence) - 1]['price'] * int(del_num)
                            if tol_money < int(money):
                                break
                    print('请结账')
                    break



        else:
            print('请输入水果名字对应序号，不要超出范围')
    else:
        print('请输入数字')

