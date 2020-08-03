"""
自定义模块
模块就是一个py文件常用的相似的功能集合。
优点：拿来主义，提高开发效率
便于维护
模块的分类：1.内置模块200种左右，Python解释器自带的模块，time、os、sys、hashlib等
2.第三方模块，一些大神写的，需要pip、install，比如Django、request、flask、Beautiful_soup
3.自定义模块
"""
#导入自定义模块时会自动执行可执行的语句(在原模块上加if __name__ == '__main__'就不会）
# 系统导入模块的路径：1.按照python的路径下，Lib
# 2.sys.path 是一个列表，可以导入模块的路径
# import a
# import a  先从内从中找模块，如果有的话从内存中加载（被导入模块有独立的内存空间）
# import sys
# print(sys.path)  #可以导入模块的路径
# print(__file__)  #打印当前文件的路径

# from xxx import a 从某个模块导入a成员
# from xxx import * 从某个模块导入所有成员
from a import b  #__all__ = []可以控制导入的成员，与*配合使用，只对from a import *有用
# 将a模块中的b变量地址导入到本模块的名称空间中，会与本模块的变量冲突，更改b变量的
# 值更改本模块中的b，不会更改a模块中的b的值
# 当导入函数时导入的是函数的内存地址，本模块执行时会去a模块中执行
# import a
# 本模块的名称空间借用    a模块的名称空间，更改a模块里面的变量只对a模块有影响