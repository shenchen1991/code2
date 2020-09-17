import socket

# 创建socket连接
# AF_INET:表示这个socket使用来进行网络连接
# SOCK_DGRAM：表示连接是一个udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9090))
while True:
    data, address = s.recvfrom(1024)
    print(data.decode('utf-8'), address[0], address[1])
    if data.decode('utf-8') == 'stop':
        break
s.close()

# 创建socket连接
# AF_INET:表示这个socket使用来进行网络连接
# SOCK_DGRAM：表示连接是一个TCP连接
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 8080))
# s.listen(128)
# client_socket, client_address = s.accept()
# x = client_socket.recv(1024)
# print(x.decode('utf-8'))
# print(client_address)
# s.close()
