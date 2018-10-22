from time import sleep
import threading

def worker():
    print('I have started.')
    sleep(5)
    print('I have exited.')

t = threading.Thread( target=worker, daemon=True)
t.start()

print('Main thread exit.')
