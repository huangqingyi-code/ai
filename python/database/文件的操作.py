# 读
# read（）全部读出来，readline（）读一行，readlines（）全部读出来作为一个列表：
# with open('log',mode='r',encoding='utf-8')as f1:
#     content1 = f1.read()
#     print(f1.tell())
#     f1.seek(0)
#     content2 = f1.readlines()
#     f1.seek(0)
#     content3 = f1.readline()
# print(content1,content2,content3)
import hashlib
import time
a = time.time()
with open('register', mode='rb')as f:
    content = f.read()
    ret = hashlib.md5()
    ret.update(content)
    print(ret.hexdigest())
b = time.time()
print(b-a)

a1 = time.time()
with open('register', mode='rb') as f1:
    content1 = 1
    ret1 = hashlib.md5()
    while content1:
        content1 = f1.read(1024)
        ret1.update(content1)
    print(ret1.hexdigest())
b1 = time.time()
print(b1-a1)