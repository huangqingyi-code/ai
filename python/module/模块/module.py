# 导入模块的搜素路径
# 1.先从内存中找 2.从内置模块中3.从sys.path
# 模块：1.内置模块2.第三方模块：django，request，flask
# if __name__ == '__main__'
# __all__ = ['a'] 仅针对from a import * 调用方法，只调用[]列表里面的变量/方法
# from a import * 容易覆盖本模块相同名字的变量，调用方便
#第一导入模块时先从内存查找，没有的话会把模块执行一次；后面再次导入时不会执行
# import执行两步骤：先开辟一个名称空间，执行导入模块的内容，
import sys
import os
# print(sys.path)
# print(__file__)
# def fun():
#     print(666)
# from a import *
# fun()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(sys.path)
import day01.classcall