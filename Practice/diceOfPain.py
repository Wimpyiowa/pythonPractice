#random

import random

a = random.random() #Prints a float from 0-1
print(a)

a = random.uniform(1, 10) #Basically above, but has a longer range now, given by an input.
print(a)

a = random.randint(1, 10) #now prints an integer !
print(a)

a = random.randrange(1, 10) #Prints a range, but will never pick the upper end. So, it doesn't print 10. Why would you ever fucking want this stupid function. Also, prints an integer.
print(a)

a = random.normalvariate(0,1) #Statistic shit.
print(a)

myList = list("ABCDEFGH") #Wow, it selects values from this list! But never prints out the same value twice. There is a function on the next indent though !
a = random.sample(myList, 3)
print(a)

myList = list("ABCDEFGH") #Now we can possibly get the same values !
a = random.choices(myList, k=3)
print(a)

myList = list("ABCDEFGH") #Self explainitory
random.shuffle(myList)
print(myList)

random.seed(1)

print(random.random())
print(random.randint(1, 10))

random.seed(1)

print(random.random())
print(random.randint(1, 10))
#These seeds act as memory. So, these outputs have the same memory that cannot be overwritten.
#Not recommended for secruity.

import secrets

a = secrets.randbelow(10) #Has a upperbound, so 10 will not be included.
print(a)

a = secrets.randbits(4) #Highest number here would be 15
print(a)

myList = list("ABCDEFGH")
a = secrets.choice(myList)
print(a)

#NumPy
import numpy as np

a = np.random.rand(3) #Prints three random floats
print(a)

a = np.random.rand(3, 3) #More dimensions. This is now 3x3
print(a)

a = np.random.randint(0, 10, 3) #Three indicates how much values are printed
print(a)

a = np.random.randint(0, 10, (3,4)) #Is now 3x4. 
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
print(arr)
np.random.shuffle(arr) #Shuffles only the first elements
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))