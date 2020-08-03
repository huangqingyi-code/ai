# class Person():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.job = 'teacher'  #相当于默认参数，不用传参
# # wusir = Person('wusir',30,'boy')
# # wusir.money = 0  #增
# # del wusir.sex    #删
# # wusir.age = 18   #改
# # print(wusir.__dict__)
#     def attcak(self,dog):
#         print(dog.hp)
#
# class Dog():
#     def __init__(self,name,hp):
#         self.dog_name = name
#         self.hp = hp
# 小白 = Dog('小白',3)
# alex = Person('alex',18,'male')
# alex.attcak(小白)

# 实例化：
# 实例=类名（）
# 首先开辟空间，调用init方法，把开辟的空间地址传递给self参数
# init方法中一般完成：把属性的值存储在self空间里——对象的初始化
# self这个地址会作为返回值，返回给实例

# 继承
class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name}eats food')

class dog(Animal):
    def __init__(self,name,age,color):
        Animal.__init__(self,name,age)
        self.color = color
xiaobai = dog('小白',2,'灰色')
print(xiaobai.__dict__)


# class dog(Animal):
#     def eat(self):
#         print('dog is eating')
#         Animal.eat(self)
# 小白 = dog('xiaobai',5)
# # print(小白.__dict__)
