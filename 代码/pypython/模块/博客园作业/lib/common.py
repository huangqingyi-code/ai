""""放置装饰器和日志函数"""
from scr import scr
def decorate(fuc):
    def inner(*args,**kw):
        if scr.state_dic['state']==True:
            ret = fuc(*args,**kw)
            return ret
        else:
            scr.login()
            ret = fuc(*args,**kw)
            return ret
    return inner