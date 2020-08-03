import sys
import os
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from scr import scr
def run():
    dic = {1:scr.login,
           2:scr.register,
           3:scr.article,
           4:scr.comment,
           5:scr.diary,
           6:scr.collect,
           7:scr.registration,
           8:scr.out}
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
if __name__=='__main__':
    run()