""""放主逻辑函数"""
from config import  setting
from lib import common
state_dic = {'state':False,'name':None}
def get_code():
    with open(setting.path,encoding='utf-8',mode='r')as f1:
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
# def decorate(fuc):
#     def inner(*args,**kw):
#         if state_dic['state']==True:
#             ret = fuc(*args,**kw)
#             return ret
#         else:
#             login()
#             ret = fuc(*args,**kw)
#             return ret
#     return inner
@common.decorate
def article():
    print('欢迎进入文章页面')
@common.decorate
def comment():
    print('欢迎进入评论页面')
@common.decorate
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