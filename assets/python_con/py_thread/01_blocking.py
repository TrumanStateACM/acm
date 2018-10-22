from timer import Timer
from time import sleep
import random

def task():
    sleep(random.randint(0,5))



print("Begin")
timer = Timer()
for i in range(5):
    task()
    print("Task {0} done".format(i))
    timer.now()

