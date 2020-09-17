import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

file_name = input('请输入你需要下载的文件名称：')

s.send(file_name.encode('utf-8'))

with open('temp_' + file_name, 'wb') as file:
    while True:
        content = s.recv(1024)
        if not content:
            break
        file.write(content)

s.close()
