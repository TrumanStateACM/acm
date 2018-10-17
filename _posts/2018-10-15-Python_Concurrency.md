---
layout: post
title: "Python Concurrency"
date: 2018-10-15
categories: meeting minutes
---

## Topic: Python Concurrency

python basics

- uses white space instead of brackets

```python
for i in range(5):
    stuff
```

Concurrency

- used to programs that execute on one thread that runs from start to finish and you can trace it 
- concurrency allows multiple tasks to be preformed at once
- have to wait for threads to finish before we exit the main program
```python
t.join()
```

- this all allows for more work to be done in less time. 

Python has some oddities
- to pass in arguments you have to make it known you are passing in tuples not other data types
```python
v = (5) \\int
v = (5,) \\tuple
```

Threading in Python specifically

- Using the basic threading package in python, all threads are run on the same python thread.
    - this means that three threads in your program are running on the one thread on your computer
    - this ends up making threading run slower in many scenarios
- the operating system gives the python interpreter a single core and then the python interpreter has to schedule the three threads on its own which can lead to it taking longer than linear execution 
- what is the use of threading if it slows down the program

Blocking and non-blocking

- blocking is basically something that requires the program or thread to wait for something
    - such as sleeping or waiting for network traffic

Sharing memory
- when you have shared memory, multiple threads have access to the same data
- when the scheduler doesn't overlap execution of the threads, you can get the right answer
    - other times you cannot
- an example is adding and subtracting at the same time in two different times
    - one run got 0, the desired answer
    - the second run got -30549
- we often do not want memory accessed at the same time

Semaphore 
- how do you make sure data isn't edited concurrently
- you often use locks
```
self.lock = threading.lock



s.lock.aquire()
stuff
s.lock.release()
```

- this allows for a thread to deny access to memory while it executes
- for logic that requires constant locking of data, this can make threading slower than linear due to overhead 

This doesnt sound good. when would you use threads
- think of accessing a first in first out queue and producer and consumer example(you can google this if you dont know what that is)
    - the threads should not be looking at the same part of the queue very often
    - this means, there shouldnt be many times when one thread is locked out of the queue making it much faster to thread it
- so try to group and minimize the code using the memory
- if you have a lot of blocking code this is also good

Daemon threads
- normal threads will keep running after the main thread or main program has ended
- a Daemon thread will stop running the second the main thread exits
    - even if its not finished, the thread will close
    - this is dangerous if say the thread is accessing the file

Multiprocessing
- This is actually using multiple processors on the computer
- this allows for true actual concurrency
- python is no longer using a scheduler

In python threading is different than multiprocessing
- threading is using one hardware thread while multiprocessing is using multiple hardware threads
- the python interpreter can only ever run one thread. it is a single threaded processor regardless
    - to do true multiprocessing, python will open a new interpreter for each processes in your program
    - a pipe is then created to pass your program to the new interpreter
        - this can lead to slow downs if your program requires large parameters to be passed
    - this copying of your program allows a small window a python interpreter is running without your code
    - it is possible for a malicious program to insert code into this interpreter and run it using the permission of your parent program
        - if your program is running in sudo, malicious code can get sudo access
    - this is fixed by using cryptographic handshakes to make sure your code is running and not malicious code

Asyncio
- scheduler only knows if a thread is blocked or not blocked
    - this can lead to some overhead of polling the threads 
- async allows for threads to declare when they are no longer blocking kind of
```python
async def name():
    code to run
```
- allows threading without as much overhead
- similar thing is there in node.js
    - kind of where it comes from 
