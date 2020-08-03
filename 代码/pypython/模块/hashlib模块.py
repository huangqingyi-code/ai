# hashlib模块
# 包含很多加密算法：MD5,sha1/sha256/sha512....
# 用途：1.密码加密，不能以明文的形式存储密码
# 2.文件的校验
import hashlib

# md5用法：1.将bytes数据类型转化成固定长度的十六进制数字组成的字符串
# 2.不同的bytes利用相同的算法（MD5）转换的结果一定不同
# 3.相同的bytes利用相同的算法（MD5）转换的结果一定相同
# 4.hashlib是不可逆的（MD5被中国王晓云破解了）
# s1 = 'fsafsgsgwt'
# ret = hashlib.md5()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest())

# 加盐：使加密更复杂，避免黑客撞库破解。
# s1 = 'dfasdffdf'
# ret = hashlib.md5('太白金星'.encode('utf-8')) #加动态盐 '太白金星‘[::2]
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest())

# sha系列数字越高加密越复杂，越不易破解，耗时长（金融、安全类的公司使用）
# s1 = 'afasf'
# ret = hashlib.sha3_512()
# ret.update(s1.encode('utf-8'))
# print(ret.hexdigest())

# 文件的校验
# 一切皆文件：下载的视频、软件（国外的软件会提供MD5值）、文件
#下载完后校验两者的MD5值是否一样就可以判断文件是否完整或者在下载过程中有没有被植入病毒
s1 = '中'
s2 = '国'
import hashlib
# def encription(file):
ret = hashlib.md5()
ret.update(s1.encode('utf-8'))
ret.update(s2.encode('utf-8'))
print(ret.hexdigest())
# print(ret.hexdigest())  #80c7fad305b8eef22f7775002c81cde5
    # return ret.hexdigest()