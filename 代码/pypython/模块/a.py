# __all__ =['b']
# __all__是一个列表，用于本列表可以被外界使用的,仅对于from a impo *有效，对于impor a无效
b = 1
print(id(b))
c = 2
import time
def print_time():
    print(time.time())
def main():
    print_time()
    for i in range(5):
        print(i)
#脚步方式运行时，__name__ 是 __main__
# 以导入方式运行时,__name__ 是模块的名字a
# print(__name__)
if __name__ == '__main__':
    main()

