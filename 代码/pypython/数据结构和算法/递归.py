# 递归函数：
# 了解什么是递归函数：在函数中调用自身的函数
# 最大的递归深度默认是997/998---python从内存角度出发做的限制（可以自己更改）
# import sys
# sys.setrecursionlimit(1000)
# n = 0
# def story():
#     global n
#     n +=1
#     print(n)
#     story()
# story()
# 递归算法特点：
# 1.如果递归次数太多，就不适合用递归来解决问题
# 2.递归的缺点：占内存
# 3.递归的有点：代码简洁
# 一个递归函数

# 斐波拉契数列
# 1,1,2,3,5,8....
# def fib(n):
# #     if n==1 or n==2:
# #         return 1
# #     else:
# #         return fib(n-1)+fib(n-2)
# # print(fib(12))
# def f(n):
#     if n ==1:
#         return 1
#     else:
#         return n*f(n-1)
# print(f(3))

# 题一：查看一个文件夹下所有的文件
import os
# def show_file(path):
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         abs_path = os.path.join(path,name)
#         if os.path.isfile(abs_path):
#             print(name)
#         elif os.path.isdir(abs_path):
#             show_file(abs_path)
# show_file(r'C:\Users\Administrator\PycharmProjects\study\python\模块')

# def work_size(path):
#     size = 0
#     name_list = os.listdir(path)
#     # print(name_list)
#     for name in name_list:
#         abs_path = os.path.join(path,name)
#         # print(abs_path)
#         if os.path.isfile(abs_path):
#             size += os.path.getsize(abs_path)
#         elif os.path.isdir(abs_path):
#             ret = work_size(abs_path)
#             size +=ret
#     return size
# res = work_size(r'C:\Users\Administrator\PycharmProjects\study\python\模块\博客园作业')
# print(res)

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
# print(menu['北京'])
# def find(menu):
#     while True:
#         for i in menu:
#             print(i)
#         key = input('输入名字').strip()
#         if menu.get(key):
#             dic = menu[key]
#             ret = find(dic)
#             if not ret:return None
#         elif key.upper()=='B':
#             return True
#         elif key.upper()=='Q':
#             return False
#
# ret = find(menu)
def fun(number):
    a = 0
    while True:
        print(a)
        return False

fun(4)

