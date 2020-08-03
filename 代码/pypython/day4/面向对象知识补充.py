class Coruse():
    def __init__(self,cours,price,period):
        self.course = cours
        self.price = price
        self.period = period
python = Coruse('python',21800,'六个月')
linux = Coruse('linux',19800,'五个月')
import pickle
# with open('course',mode='wb')as f1:
#     pickle.dump(python,f1)
#     pickle.dump(linux,f1)
with open('course',mode='rb')as f1:
    ret = pickle.load(f1)
    print(ret)
    ret = pickle.load(f1)
    print(ret)