import multiprocessing, queue

mq = multiprocessing.Queue(5)
q = queue.Queue

mq.put('hello')
mq.put('hello')
mq.put('hello')
mq.put('hello')
mq.put('hello')
mq.get()
mq.put('hello')


