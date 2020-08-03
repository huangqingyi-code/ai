# import socket
# sk = socket.socket()
# sk.connect(("127.0.0.1",9000))
#
#
# msg = sk.recv(1024)
# print(msg)
# sk.send(b'byebye')
# sk.close()

#与server端一直对话
# import socket
# sk = socket.socket()
# sk.connect(("127.0.0.1",9000))
# while True:
#     msg1 = sk.recv(1024).decode("utf-8")
#     if msg1.upper()=="Q":break
#     print(msg1)
#     msg = input("<<<<<<")
#     sk.send(msg.encode("utf-8"))
#     if msg.upper() == "Q": break
#
# sk.close()

import socket
import time
import json
import os
sk = socket.socket()
sk.connect(("127.0.0.1",9001))
size = os.path.getsize("f1")
path = r"C:\Users\Administrator\Desktop\资料\数字图像处理_第三版_中_冈萨雷斯.pdf"

print(os.path.basename(path))
print(os.path.getsize(path))
content = 1
with open(path,mode="rb")as f:
    while content:
        content = f.read(1024)
        sk.send(content)
sk.close()






