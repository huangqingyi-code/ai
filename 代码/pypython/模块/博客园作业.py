'''
作业：用代码模拟博客园系统。
项目分析：
一．首先程序启动，页面显示下面内容供用户选择：
1.请登录
2.请注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序
二．必须实现的功能：
1.注册功能要求：
a.用户名、密码要记录在文件中。
b.用户名要求：只能含有字母或者数字不能含有特殊字符并且确保用户名唯一。
c.密码要求：长度要在6~14个字符之间。
d.超过三次登录还未成功，则退出整个程序。
2.登录功能要求：
a.用户输入用户名、密码进行登录验证。
b.登录成功之后，才可以访问3~7选项，如果没有登录或者登录不成功时访问3~7选项，
不允许访问，让其先登录。（装饰器）
3.进入文章页面要求：
a.提示欢迎xx进入文章页面。
b.此时用户可以选择：直接写入内容，还是导入md文件。
①如果选择直接写内容：让学生直接写文件名|文件内容......最后创建一个文章。
②如果选择导入md文件：让用户输入已经准备好的md文件的文件路径
（相对路径即可：比如函数的进阶.md），然后将此md文件的全部内容写入文章
函数的进阶.text）中。
4.进入评论页面要求：
提示欢迎xx进入评论页面。
5.进入日记页面要求：
提示欢迎xx进入日记页面。
6.进入收藏页面要求：
提示欢迎xx进入收藏页面。
7.注销账号要求：
不是退出整个程序，而是将已经登录的状态变成未登录状态（访问3~7选项时需要重新登录）。
8.退出整个程序要求：
就是结束整个程序。
'''
state_dic = {'state':False,'name':None}
def get_code():
    with open('register',encoding='utf-8',mode='r')as f1:
        code_dic = {}
        for i in f1:
            list = i.strip().split('|')
            code_dic[list[0]] = list[1]
    return code_dic
def login():
    use_dic = get_code()
    count = 0
    while count<3:
        use_name = input('请输入用户名')
        use_psw = input('请输入密码')
        if use_name in use_dic and use_dic[use_name]==use_psw:
            print('登录成功')
            state_dic['name'] = use_name
            state_dic['state'] = True
            return True
        else:
            print('用户名或密码错误，您还有%s次机会'%(2-count))
            count += 1
import hashlib
def encryption(code):
    ret = hashlib.md5()
    ret.update(code.encode('utf-8'))
    return ret.hexdigest()
def register():
    while 1:
        name = input('请输入注册用户名，输入Q退出注册')
        if name.upper()=='Q':
            break
        psw = input('请输6-14字符的密码')
        use_dic = get_code()
        if name in use_dic:
            print('该用户名已注册，请重新输入')
        else:
            if 6<len(psw)<14 and name.isalnum():
                code_psw = encryption(psw)
                with open('register',encoding='utf-8',mode='a')as f2:
                    f2.write(f'\n{name}|{code_psw}')
                break
            else:
                print('请输入合法的用户名or密码')
def decorate(fuc):
    def inner(*args,**kw):
        if state_dic['state']==True:
            ret = fuc(*args,**kw)
            return ret
        else:
            login()
            ret = fuc(*args,**kw)
            return ret
    return inner
@decorate
def article():
    print('欢迎进入文章页面')
@decorate
def comment():
    print('欢迎进入评论页面')
@decorate
def diary():
    print('欢迎进入日记页面')
def collect():
    print('欢迎进入收藏页面')
def registration():
    state_dic['state'] = False
    state_dic['name'] = None
def out():
    # import sys
    # sys.exit()
    import os
    os._exit(0)
def run():
    dic = {1:login,
           2:register,
           3:article,
           4:comment,
           5:diary,
           6:collect,
           7:registration,
           8:out}
    while 1:
        print('''
            1.请登录
            2.请注册
            3.进入文章页面
            4.进入评论页面
            5.进入日记页面
            6.进入收藏页面
            7.注销账号
            8.退出整个程序
            ''')
        num = input('请输入要执行功能的序号').strip()
        if num.isdigit()and (int(num) in [i for i in range(1,9)]):
            dic[int(num)]()
        else:
            print('请输入正确的序号')
run()