#python 默认最大递归深度1000，出于节省内存
# 递归更占用内存，能不用就不用
# 必须要有结束递归的条件，return
# 并不是递归函数中有return外层调用函数就有返回值
import sys
# sys.setrecursionlimit(1000)
count = 0
def fun():
    global count
    count += 1
    print(count)
    # if count == 3:
    #     return count
    ret = fun()
    # return ret
    # return fun()
    # print(666)
# print(fun())

# 1.exercise:factorial
def factorial(n):
    if n == 1:return n
    else:
        return n * factorial(n-1)
# print(factorial(5))
# 2.fibonacci sequence 1,1,2,3,5,8,13,21,34,55
def fibonacci1(n):
    if n==1 or n==2:
        return 1
    else:return fibonacci1(n-1) + fibonacci1(n-2)
# print(fibonacci1(40))
def fibonacci(n):
    a,b = 1,1
    while n >2:
        a,b = b,a+b
        n -= 1
    return b
# print(fibonacci(100))

#3.exercise 查看文件夹下所有的文件
import os
# def show_file(path):
#     name_list = os.listdir(path)
#     for i in name_list:
#         abs_path = os.path.join(path,i)
#         if os.path.isfile(abs_path):
#             print(abs_path)
#         elif os.path.isdir(abs_path):
#             show_file(abs_path)
# show_file(r"C:\Users\Administrator\Desktop\代码\pypython\模块")

def get_size(path):
    name_list = os.listdir(path)
    size = 0
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            size += os.path.getsize(abs_path)
        else:
            # return get_size(abs_path)
            ret = get_size(abs_path)
            size += ret
    return size
# print(get_size(r"C:\Users\Administrator\Desktop\代码\pypython\模块"))

# 4.menu
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
def look(menu):
    flag = True
    while flag:
        for name in menu:
            print(name)
        key = input("<<<input where you want to look").strip()
        if menu.get(key):
            new_menu = menu[key]
            flag =look(new_menu)
        elif key.upper() == 'B':
            return True
        elif key.upper() == 'Q':
            return False
        else:print('no this name')
print(look(menu))
print('wahaha')