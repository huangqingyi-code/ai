# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __add__(self, other):
#         return self.age + other.age
# wusir = Person('wusir',18)
# alex = Person('alex',18)
# taibai = Person('taibai',20)
# print(wusir+alex)
# print(id(a),id(b))

class Mylist:
    def __init__(self,iterable=()):
        self.data = list(iterable)
    def __add__(self, other):
        return Mylist(self.data+other.data)

L1 = Mylist((1,2,3))
print(L1.__dict__)
L2 = Mylist([4,5,6])
print((L1+L2).data)