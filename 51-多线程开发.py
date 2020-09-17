import threading
import time

ticket = 200

lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()
        if ticket > 0:
            # time.sleep(1)
            ticket -= 1
            lock.release()
            print('{}卖出票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            lock.release()
            print('卖完了')
            break


t1 = threading.Thread(target=sell_ticket)
t2 = threading.Thread(target=sell_ticket)
t3 = threading.Thread(target=sell_ticket)
t4 = threading.Thread(target=sell_ticket)
t5 = threading.Thread(target=sell_ticket)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
