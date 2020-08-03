import os
def loggin(acount,psw):
    with open('register',mode='r',encoding='utf-8')as f1:
        for line in f1:
            a,b = line.strip().split('|')
            if a==acount and b==psw:
                print('登录成功')
                return b
class Operation():
    def __init__(self,use_name,use_psw):
        self.use_name = use_name
        self.use_psw = use_psw
    def chang_code(self):
        ret = loggin(name, password)
        old_code = input('请输入旧密码')
        if old_code==ret:
            new_code = input('请输入新密码')
            with open('register',encoding='utf-8',mode='r')as f1,\
            open('new_register',encoding='utf-8',mode='w')as f2:
                for line in f1:
                    a,b = line.strip().split('|')
                    if a==name:
                        f2.write(f'{name}|{new_code}\n')
                    else:f2.write(f'{line}\n')
            os.remove('register')
            os.rename('new_register','register')
        else:print('密码输入错误')

name = input('请输入账号名')
password = input('请输入密码')
obj = Operation(name,password)
obj.chang_code()