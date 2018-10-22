from time import sleep

import threading
import queue

#https://docs.python.org/3.7/library/queue.html

TIME_PROD = 2
TIME_CONS = 1

def producer(q):
    for i in range(10):
        print('Produced item {0}.'.format(i))
        sleep(TIME_PROD)
        q.put(i)
        print('Done.')
    q.put(None)

def consumer(q):
    d = q.get()
    while d != None:
        print('\t\t\t Processing item {0}.'.format(d))
        work = d * 2 - 3
        sleep(TIME_CONS)
        print('\t\t\t Done. Result is {0}.'.format(work))
        d = q.get()


comm = queue.Queue()

print("Begin")
tc = threading.Thread(target = consumer, args=(comm,))
tp = threading.Thread(target = producer, args=(comm,))
tc.start()
tp.start()
tc.join()
tp.join()

print("Done")

