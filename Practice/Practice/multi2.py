from threading import Thread
import os
import time

def square_number():
    for i in range(100):
        i * i
        time.sleep(0.1)


threads = []
num_threads = 10

#create processes
for i in range(num_threads):
    t = Thread(target=square_number)
    threads.append(t)

#Start
for t in threads:
    t.start()

#join
for t in threads:
    t.join()

print('end main')