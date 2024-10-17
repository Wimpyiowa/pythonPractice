with open('notes.txt', 'w') as file: #Easier way to write into files
    file.write('some todoo...')

file = open('notes.txt', 'w') #Takes longer to write
try:
    file.write('some todoo...')
finally:
    file.close()

#Lock
from threading import Lock
lock = Lock()

lock.acquire()
#...
lock.release()

#with lock:
    #...

#Example 2
class ManageFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
            if exc_type is not None:
                print('exception has been handled')
        #print('exc:', exc_type, exc_value)
        print('exit')
        return True

with ManageFile('notes.txt') as file:
    print("do some stuff...")
    file.write('some todoo...')
    file.somemethod()

print('countinuing')

#Function
from contextlib import contextmanager

@contextmanager
def open_mananged_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()

with open_mananged_file('notes.txt') as f:
    f.write('some todoo...')