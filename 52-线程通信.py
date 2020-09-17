import queue
import threading


def produce():
    for i in range(10):
        print('生产了面包b{}'.format(i))
        q.put('b{}'.format(i))


def consumer():
    for i in range(50):
        print('买到了面包{}'.format(q.get()))


q = queue.Queue()

p1 = threading.Thread(target=produce, name='p1')
c1 = threading.Thread(target=consumer, name='c1')

p1.start()
c1.start()
