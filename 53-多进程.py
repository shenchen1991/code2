import multiprocessing
import os
import time


def dance(n):
    for i in range(n):
        time.sleep(.5)
        print('dance', os.getpid())


def sing(n):
    for i in range(n):
        time.sleep(.5)
        print('sing', os.getpid())


if __name__ == '__main__':
    # args 用于传参 是一个元组
    p1 = multiprocessing.Process(target=dance, args=(10,))
    p2 = multiprocessing.Process(target=sing, args=(30,))

    p1.start()
    p2.start()
