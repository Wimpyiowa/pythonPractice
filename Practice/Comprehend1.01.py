#Tuples 

mytuple = ("Max", 25, "Boston")
print(mytuple)

item = mytuple[-1]
print(item)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print ("no")

letterTuple = ('a', 'p', 'l', 'l')


print(len(letterTuple)) #Check the length of a tuple.

print (letterTuple.count("l")) #Counts how many of the value is in the tuple

print (letterTuple.index("p")) #Finds the index of this value, where it first appears.

my_list = list(letterTuple) #Converts tuple into a list.
print(my_list)

my_tuple2 = tuple(my_list) #Converts back to a tuple.
print(my_tuple2)

a = (1,2,3,4,5,6,7)

b = a[::2]
print(b)

name, age, city = mytuple #Assigning values into a variable.
print(name)
print(age)
print(city)

i1, *i2, i3 = mytuple #Converts into a list, and will grab these values based off their index number.

print(i1)
print(i3)
print(i2)

import sys
my_list = [0,1,2, "hello", True] #Return the amount of bytes a dataset has. Lists are larger than tuples in this example.
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(mytuple), "bytes")


import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) #Calculate how long these take to make. In this example, it took longer for a list to be made.
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))


