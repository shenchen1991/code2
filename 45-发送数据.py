import socket

# 创建socket连接
# AF_INET:表示这个socket使用来进行网络连接
# SOCK_DGRAM：表示连接是一个udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("输入：")
    s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    if msg == 'stop':
        break
s.close()

# 创建socket连接
# AF_INET:表示这个socket使用来进行网络连接
# SOCK_STREAM：表示连接是一个tcp连接
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# while True:
#     msg = input("输入：")
#     s.connect(('127.0.0.1', 8080))
#     s.send(msg.encode('utf-8'))
#     if msg == 'stop':
#         break
# s.close()
