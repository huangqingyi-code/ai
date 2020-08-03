# 正则表达式作用：1.检测一个输入的字符串是否合法（用户输入一个内容的时候，我们要提前
# 检测，能够提高程序的效率并且减轻服务器的压力
# 2.从一个大文件中找到所有符合规格的内容
# 字符组 描述的是一个位置上能出现的所有可能性
    # 接受范围,可以描述多个范围,连着写就可以了
    # [abc]   一个中括号只表示一个字符位置
    # 匹配a或者b或者c
    # [0-9]   根据ascii进行范围的比对
    # [a-z]
    # [A-Z]
    # [a-zA-Z] 大小写
    # [0-9a-z]
# a表达式|b表达式     匹配a或者b表达式中的内容,如果匹配a成功了,不会继续和b匹配
#                       所以,如果两个规则有重叠部分,总是把长的放在前面
# ()    # 约束 | 描述的内容的范围问题

# www\.oldboy\.com|www\.baidu\.com|www\.jd\.com|www\.taobao\.com
# www\.(oldboy|baidu|jd|taobao)\.com
# 转义符
    # 原本有特殊意义的字符,到了表达它本身的意义的时候,需要转义
    # 有一些有特殊意义的内容,放在字符组中,会取消它的特殊意义
        # [().*+?] 所有的内容在字符组中会取消它的特殊意义
        # [a\-c]  -在字符组中表示范围,如果不希望它表示范围q,需要转义,或者放在字符组的最前面\最后面
# split
#sub
# search  只查找一个，找到即停
# match 从头开始匹配，找到一个即停
# compile --节省代码时间的工具：加入同一个正则表达式被多次使用，可以节省解析的时间
#finditer---节省空间
#先compile（正则被多次使用）和finditer（返回的结果很多）可以节省时间和空间
import re
# ret = re.compile('\d+')
# res1 = ret.finditer('alex4235fsdff645647')
# for i in res1:
#     print(i.group())

# ret1 = re.split('\d+','alex123wusir')   #['alex', 'wusir']
ret2 = re.split('(\d\d\d)','alex123wusir')   #['alex', '2', 'wusir']
print(ret2)
# ret3 = re.sub('\d+','H','alex123wusir')   #alexHwusir
# print(ret3)