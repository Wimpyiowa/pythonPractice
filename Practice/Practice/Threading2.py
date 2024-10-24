from threading import Thread, Lock, current_thread
from queue import Queue
import os
import time

#Example
def worker(q, lock):
    while True:
        value = q.get()
        #Processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ =="__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread3 = Thread(target=worker, args=(q, lock))
        thread3.daemon=True #This is a background thread that will die once the main thread dies
        thread3.start()

    for i in range (1, 21):
        q.put(i)
    
    q.join()

    print('end main')