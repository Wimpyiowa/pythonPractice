def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

#for i in g:
    #print(i)

value = next(g) #Stops at yield 1.
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

#value = next(g) #Will get an error until you give another yield statement
#print(value)

print(sum(g)) #Should be six, but all values are counted.

sorted(g) #Sorts by lowest to highest number.

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num) 
        num += 1
    return nums

print(firstn(10))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000))) #Loop takes way more memory
print(sys.getsizeof(firstn_generator(1000))) #Generator takes much less memory

#Example 3

def fibonacci(limit):
    # 0 1 1 2 3 4 5 8 13
    a, b = 0,1 
    while a < limit:
        yield a
        a, b = b, a + b
fib = fibonacci(30)
for i in fib:
    print(i)

#4

mygenerator = (i for i in range(10) if i % 2 ==0)
for i in mygenerator:
    print(i)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10) if i % 2 ==0]
print(mylist)
print(sys.getsizeof(mylist))

