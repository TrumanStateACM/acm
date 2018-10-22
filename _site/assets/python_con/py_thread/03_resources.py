from timer import Timer
import threading

def prime_test(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            print(n, "is NOT prime")
            return
    print(n, "is prime!")


test = [179424743, 179857437, 179425619]


print('Linear')
timer1 = Timer()
for n in test:
    prime_test(n)
    timer1.now()
print('Done')
timer1.now()


print()


print('Threaded')
timer2 = Timer()

threads = []
for n in test:
    t = threading.Thread(target = prime_test, args=(n,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print('Done')
timer2.now()

