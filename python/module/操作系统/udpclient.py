import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

server = ("127.0.0.1",9000)
sk.sendto(b'info',server)
msg = sk.recv(1024)
print(msg)
