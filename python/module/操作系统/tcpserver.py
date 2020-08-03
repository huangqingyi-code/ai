# import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1",9000))  #向操作系统申请资源（端口）
# sk.listen()
#
# conn,addr = sk.accept()   #conn里存储的是client和server端的连接信息
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg)
# conn.close()    #挥手断开连接
#
# sk.close()    #向操作系统归还资源

#与client一直对话
# import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1",9000))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     while True:
#         msg1 = input("<<<<<<")
#         conn.send(msg1.encode("utf-8"))
#         if msg1.upper()=="Q":break
#         msg2 = conn.recv(1024).decode("utf-8")
#         if msg2.upper() == "Q": break
#         print(msg2)
#     conn.close()
#
# sk.close()


import socket
import json
import time
import pickle
sk = socket.socket()
sk.bind(("127.0.0.1",9001))
sk.listen()
conn,addr = sk.accept()

with open("figure.pdf",mode="wb")as f:
    while True:
        msg = conn.recv(1024)
        if not msg: break
        f.write(msg)
conn.close()
sk.close()