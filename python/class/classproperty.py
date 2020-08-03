from math import pi
"""class Circle():
    def __init__(self,r):
        self.r = r
    def area(self):
        return pi*self.r**2
a = Circle(5)
print(a.area())    #圆的面积应该是一个属性 area()看起来很变扭"""

# class Circle():
#     def __init__(self,r):
#         self.r = r
#     @property   #金仅针对没有参数的方法，调用时不用加括号
#     def area(self):
#         return pi*self.r**2
# a = Circle(5)
# print(a.area)
# import time
# class Person():
#     def __init__(self,name,birthday):
#         self.name = name
#         self.birthday = birthday
#     @property
#     def age(self):
#         return time.localtime().tm_year - self.birthday
# alex = Person('alex',1993)
# print(alex.age)


import time
class Birthday():
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
    @property
    def age(self):
        age = time.localtime().tm_year - self.birthday
        print(f'你的年龄是{age}')
Birthday('huangqingyi',1993).age
print(time.strftime("%Y-%m-%d %H:%M:%S"))