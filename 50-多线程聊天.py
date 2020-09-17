import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8080))


def send_msg():
    while True:
        msg = input("输入：")
        s.sendto(msg.encode('utf-8'), ('127.0.0.1', 9090))
        if msg == 'stop':
            break


def receive_msg():
    while True:
        data, address = s.recvfrom(1024)
        print(data.decode('utf-8'), address[0], address[1])
        if data.decode('utf-8') == 'stop':
            break


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=receive_msg)

t1.start()
t2.start()
