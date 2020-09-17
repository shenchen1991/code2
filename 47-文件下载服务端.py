import os
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(128)

# 接收客户端请求
client_socket, client_address = server_socket.accept()
file_name = client_socket.recv(1024).decode('utf-8')

print('接收到了来自{}地址{}端口的数据，内容是{}'.format(client_address[0], client_address[1], file_name))

if os.path.isfile(file_name):
    with open(file_name, 'rb') as file:
        content = file.read()
        print(content)
        client_socket.send(content)

else:
    print('文件不存在')
