from threading import Thread, Lock, current_thread
from queue import Queue
import os
import time

database_value = 0

def increase(lock):
    global database_value

    with lock:
        local_copy = database_value

        #processing
        local_copy +=1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')

#Threads share the same data, so it is easy to share that data.

#Queue

if __name__ =="__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    #3 2 1 -->
    first = q.get()
    print(first)

    q.task_done()
    q.join()

    print('end main')

#Example
def worker(q):
    while True:
        value = q.get()
        #Processing
        print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ =="__main__":

    q = Queue()

    num_threads = 10

    for i in range(num_threads):
        thread3 = Thread(target=worker, args=(q,))
        thread3.daemon=True
        thread3.start()

    for i in range (1, 21):
        q.put(i)
    
    q.join()

    print('end main')