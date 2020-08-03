#私有变量（私有方法）不能在外部调用，只能在内部使用(要看/更改只能通过内部的方法)
#私有变量不能被子类使用
"""class User():
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd
    def look(self):
        return self.__pwd
    def change(self):
        self.__pwd = 666666
alex = User('alex',123)
# print(alex.__pwd)   报错，外部不能直接查看私有变量
alex.change()
print(alex.look())"""
# import hashlib
# class User():
#     def __init__(self,name,pwd):
#         self.name = name
#         self.__pwd = pwd
#     def __get_md5(self):
#         md5 = hashlib.md5(self.name.encode('utf-8'))
#         md5.update(self.__pwd.encode('utf-8'))
#         return md5.hexdigest()
#     def get_word(self):
#         return self.__get_md5()
# alex = User('alex','123')    #int类型为什么不能encode（'utf-8'）
# print(alex.get_word())


class A:
    def __init__(self):
        self.age = 18
    def __fun(self):
        print(666)
class B(A):
    def fun(self):
        super()._A__fun()
B().fun()