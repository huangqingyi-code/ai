# 文件操作：
# 1.文件路径(绝对路径和相对路径)
# 2.编码方式（gbk/utf-8)
# 3.操作方式（读、写）

# 一、读   for i in f: 迭代器形式，文件句柄不占内存，其他读取方式内存爆掉。
# readlines() 全部读出来，是一个列表形式，每一行是一个元素**
# readline()  一行一行读
# read() 全部读出来
# f = open('D:\BugReport.txt',mode='r',encoding='utf-8')#绝对路径
# contet = f.read()
# print(contet)
# f.close()

# f1 = open('相对路径',mode = 'r',encoding = 'utf-8')#相对路径
# print(f1.read())  #bytes转化成str格式
# f1.close()

# f2 = open('相对路径',mode = 'rb')   #以bytes数据类型呈现，用于非文字的读取和用代码存储和上传
# print(f2.read())
# f2.close()


# 二、写  write  没有这个文件名的创建，有该文件名的写的内容覆盖原有的
# f = open('log',mode = 'w',encoding = 'utf-8')
# f.write('fafas')
# f.close()

# f = open('log',mode = 'wb')
# f.write('jflaj'.encode('utf-8'))
# f.close()

# 三、追加  没有文件创建文件
# f = open('log',mode = 'a',encoding = 'utf-8')
# f.write('kjjjjjj')
# f.close()

# f = open('log',mode = 'ab')
# f.write('黄清仪'.encode('utf-8'))
# f.close

# 四、读、写  （准确说是读、追加）
# f = open('log',mode = 'r+',encoding='utf-8')
# # print(f.read())
# # f.write('jjjjjj')
# f = open('log',mode='r+b')
# print(f.read())
# f.write('lllll'.encode('utf-8'))
# f.close()

# # 五、写、读
# f = open('log',mode='w+',encoding='utf-8')
# f.write('fsdfs')
# f.seek(0)  #把光标移到最前面才能读出来,
# print(f.read())
# f.close()

# 功能详解
# f = open('log',mode='r+',encoding='utf-8')
# # file = f.read(3)  read读取的单位是字符
# # f.seek(3)         seek读取是按utf-8字节形式
# print(f.read())

# f = open('log',mode='a+',encoding='utf-8')
# f.write('发斯蒂芬')
# # f.tell()   告诉你光标的位置
# f.seek(0)  #把光标移到最前面才能读出来,
# print(f.read())
# f.close()

# f.readline()   只读一行
# f.readlines()  一行作为一个列表的一个元素
# with open('log',mode='r+',encoding='utf-8') as f:  #with  不用close
# #     for line in f:
#         print(line )

# use_name = input('请输入注册名字')
# use_pw = input('请输入注册密码')
# with open('register',mode='w+',encoding='utf-8') as f:
#     f.write('{}|{}'.format(use_name,use_pw))
# print(f)

# with open('log',encoding='utf-8') as f1,\
#         open('register',mode='r',encoding='utf-8') as f2:
# lst = []
# item_lst = ['name','price','amount']
# with open('log',encoding='utf-8') as f1:
#     for line in f1:
#         new_line = line.strip().split()
#         dic = {}
#         for index in range(len(item_lst)):
#             dic[item_lst[index]] = new_line[index]
#         lst.append(dic)
# print(lst)

# with open(r'C:\Users\Administrator\PycharmProjects\study\python\day1\IMG_20170831_175916.jpg',
#           mode='rb')as f:
#     conten = f.read()
#     print(len(conten))
import hashlib
# def encription(file):
#     ret = hashlib.md5()
#     ret.update(file)
#     return ret.hexdigest()
with open(r'C:\Users\Administrator\PycharmProjects\study\python\day1\IMG_20170831_175916.jpg',
          mode='rb')as f,\
        open('log',mode='a',encoding='utf-8')as f1:
    ret = hashlib.md5()
    content = 1
    while content:
        content = f.read(1024)
        ret.update(content)
    res = ret.hexdigest()
    f1.write(f'\n{ret}')

# with open('log',mode='a',encoding='utf-8')as f1:
#     f1.write(f'\n{str(res)}')



# with open('log',encoding='utf-8',mode='r')as f:
#     content = True
#     while content:
#         content = f.read(10)
#         print(content)





