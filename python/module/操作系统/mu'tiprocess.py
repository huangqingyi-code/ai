# from multiprocessing import Process
# import os
# def fun(age):
#     print(os.getpid(),os.getppid(),age)
# if __name__=="__main__":
#     #只会在主进程中执行的代码
#     # print("main:",os.getpid(),os.getppid())
#     p = Process(target=fun,args=(12,))
#     p.start()#开启一个子进程，会导入父进程中的文件multiprocess.py，并执行fun()函数
#     #Linux系统不一样，不是导入父进程的文件，是直接copy父进程的内存
#     p = Process(target=fun,args=(6,))
#     p.start()#异步非阻塞,会往下执行print    两个进程并发
#     print("hello word")
#
#     #向子进程传递参数 p = Process(target=fun，args=(12,))  元组形式
#     #不能获取子进程的返回值
#     #可以同时开启多个子进程
      #p.join()同步阻塞

from multiprocessing import Process
import os
def func(name,age):
    print(f"name:{name},age:{age}")
if __name__=="__main__":
    arg = [("wusir",20),("alex",18),("taibai",28)]
    p_lst = []
    for i in arg:
        p = Process(target=func,args=i)
        p.start()  #异步并发
        p_lst.append(p)
    for i in p_lst:
        i.join()   #同步阻塞
    print("hello python")