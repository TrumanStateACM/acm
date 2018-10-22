from time import time

class Timer:
    def __init__(self):
        self.t = time()
    def now(self):
        print('Elapsed sec: {:.6f}'.format(time() - self.t))
