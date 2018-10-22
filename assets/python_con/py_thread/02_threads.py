from timer import Timer
from time import sleep
import random

import threading

#https://docs.python.org/3.7/library/threading.html

def task(tid):
    sleep(random.randint(0,5))
    print("Task {0} done".format(tid))


threads = []

print("Begin")
timer = Timer()
for i in range(5):
    t = threading.Thread(target = task, args=(i,))
    t.start()
    threads.append(t)

print("All threads started")
timer.now()

for t in threads:
    t.join()

print("All threads done")
timer.now()

