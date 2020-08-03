user_name = 'huangqingyi'
password = '931003'
i = 0
while i < 3:
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if name == user_name and pwd ==password:
        print('登录成功')
        break
    # else:
    #     print('登录失败，您还有%s次机会' %(2-i))
    #     if i - 2 == 0:
    #         result = input('是否还想再试试？Yes')
    #         if result == 'Yes'

# else:
#     print('要不要脸')    # i = 0
#                 continue
#     i += 1
