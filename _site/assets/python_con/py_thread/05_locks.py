from timer import Timer
import threading

class State:
    def __init__(self):
        self.lock = threading.Lock()
        self.n = 0

def dec(s):
    for _ in range(100000):
        s.lock.acquire()
        s.n -= 1
        s.lock.release()

def inc(s):
    for _ in range(100000):
        with s.lock:
            s.n += 1



state = State()

print("Begin")
t = Timer()
td = threading.Thread(target = dec, args=(state,))
ti = threading.Thread(target = inc, args=(state,))
td.start()
ti.start()
td.join()
ti.join()

print("Done")
print("State is {0}".format(state.n))
t.now()

