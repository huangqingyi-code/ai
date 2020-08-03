# 单分支
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
# try:
#     num = int(input('<<<<<<'))
# except :
#     print('请输入数字')
# try:
#     print(l[num-1ValueError])
# except IndexError:
#     print('请输入1到2')

# 多分支
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
# try:
#     num = int(input('<<<<'))
#     print(l[num-1])
# except ValueError:
#     print('请输入数字')
# except IndexError:
#     print('请输入1到2')

# 多分支合并
# l = ['login','register']
# for num,i in enumerate(l,1):
#     print(num,i)
# try:
#     num = int(input('<<<<'))
#     print(l[num-1])
# except (ValueError,IndexError):
#     print('请输入合法字符')

# 万能异常   万能异常永远放在异常处理的最下面
# def brows():
#     print('one')
#     jflj
# def select():
#     print('two')
# def pay():
#     print('three')
# def main():
#     l = [('浏览',brows),('选择',select),('付款',pay)]
#     while True:
#         for num,i in enumerate(l,1):
#             print(num,i[0])
#         try:
#             num = int(input('<<<<<'))
#             print(l[num-1])
#             fun = l[num-1][1]
#             fun()
#         except (ValueError,IndexError):
#             print('输入的字符串不合法')
#         except Exception as e:
#             print(e)
#             print('用户在执行%s操作后发生不可以预知的异常' % (l[num - 1][0]))
# main()
# else 分支    在try中代码不发生异常情况下执行else（比如成功发送邮件后提示发送成功）


#主动抛出异常   用于程序员调用框架时，不用于面向用户
# raise ValueError('你写的不对')
#
# #断言  语法
# assert 1==3 只接受bool值 满足条件往下走，否则报异常


# finally分支   无论try中代码是否发生异常都会执行finally（用于资源回收，关闭文件，关闭端口）
# def fun():
#     f = open('file')
#     try:
#         while True:
#             for line in f:
#                 if line.startswich('s'):
#                     return line
#     except:
#         print('there is error')
#     finally:#即使return也会先执行finally中的代码
#         f.close()

# 异常处理忠告
# try:
#     main()    在完成程序外面加异常处理是等程序测试完成后再加
# except Exception as e:
#     把e写到一个文件里，到时候可以查看程序运行过程中产生的bug