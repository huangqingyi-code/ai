'''class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = 'man'
    def say(self):
        # print('%s说了你好'%(self.name))
        print(f'{self.name}说了你好')

alex = Person('alex',18)
# alex.age = 20
# print(alex.__dict__)
alex.say()'''

#继承
# class Animal():
#     def __init__(self,sex,name):
#         self.name = name
#         self.sex = sex
#     def say(self):
#         print('hello word')
# class Cat(Animal):
#     def __init__(self,sex,name,color):
#         super().__init__(sex,name)
#         # Animal.__init__(self,sex,name)
#         self.color = color
#     def describe(self):
#         super().say()
#         print(f'{self.sex,self.name,self.color}')
# niky = Cat('male','niky','white')
# niky.describe()
"""class User():
    def __init__(self,name):
        self.name = name
class Vip_user(User):
    def __init__(self,name,level,star_time,end_time):
        # super().__init__(name)
        User.__init__(self,name)
        self.level = level
        self.star_time = star_time
        self.end_time = end_time
太白 = Vip_user('太白',10,2019.1,2020.1)
print(太白.__dict__)"""

#组合 一个类的对象是另一个对象的属性
"""class Student():
    def __init__(self,name,sex,age,number,clas,phone):
        self.name = name
        self.sex = sex
        self.age = age
        self.number =number
        self.clas = clas
        self.phone = phone
class Clas():
    def __init__(self,course,teacher,begin_time):
        self.course = course
        self.teacher = teacher
        self.begin_time = begin_time
py22 = Clas('python','taibai',2020.5)
alex = Student('alex','man',18,20,py22,13799186130)   #对象变成了一个属性
# wusir = Student('wusir','feman',18,20,'python',18250742850)
print(alex.clas.course)"""
# class Clas():
#     def __init__(self,course,teacher,begin_time):
#         self.course = course
#         self.teacher = teacher
#         self.begin_time = begin_time
# class Subject():
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
# Linux = Subject('Linux',22800,'6个月')
# Linux18 = Clas(Linux,'taibai','2020.5')
# print(Linux18.course.period)

# class Animal:
#     def __init__(self,name,food):
#         self.name = name
#         self.food = food
#         self.blood = 100
#     def eat(self):
#         print(f'{self.name}正在吃{self.food}')
# class Cat(Animal):
#     def eat(self):
#         super().eat()
#         self.blood +=100
# class Dog(Animal):
#     def eat(self):
#         Animal.eat(self)
#         self.blood +=200
# cat = Cat('kitty','猫粮')
# dog = Dog('金毛','狗粮')
# cat.eat()
# dog.eat()
# print(cat.blood,dog.blood)
# print(cat.__dict__)
