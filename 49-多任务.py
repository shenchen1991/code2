import threading
import time


def dance():
    for i in range(50):
        time.sleep(0.1)
        print('dance')


def sing():
    for i in range(50):
        time.sleep(.1)
        print('sing')


t1 = threading.Thread(target=dance)
t2 = threading.Thread(target=sing)

t1.start()
t2.start()
