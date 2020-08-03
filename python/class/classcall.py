class Person():
    def __call__(self, *args, **kwargs):
        print('hello word')
alex = Person()()   #加()直接调用__call__下面的内容
# alex()
# print(callable(alex))

class Animal:
    def __init__(self):
        self.name = 'dog'
        print('this is a dog')
dog = Animal()
# callable() 函数用于检查一个对象是否是可调用的
print(callable(dog))  #False,dog()不能执行