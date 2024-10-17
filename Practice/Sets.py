#Set: unordered, mutable, no duplicates

myset = {1,2 ,3, 1, 2}
print(myset) #Doesn't print duplicates, so 1 and 2 will only print one time.


myset.add(1)
myset.add(2)
myset.add(3)

myset.remove (3) #Will raise key error if a value is not found
myset.discard(3) #Will not raise key error

print(myset.pop())

my_set = set("Hello")
print (my_set)

for i in myset: #Prints all the values. But in this case, only 2 is printed.
    print(i)

if 1 in myset:
    print('yes')
else:
    print("no")

#Union & Intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) #This now prints out all the numbers from 0 to 9. Union combines elements.
print(u)

i = odds.intersection(evens) #Won't print anything because these elements hold different values
print(i)

i = odds.intersection(primes) #This will print out all the numbers that are found in negative prime numbers
print(i)

#Difference of sets

setA = {1, 2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB) #Will print out the numbers that are differet from setB. This can also be swapped, printing out setB values.
print(diff)

diff = setB.symmetric_difference(setA) #Will print out all the different numbers, but not the numbers that show up in both sets.
print(diff)

setB.update(setA)
print(setB) #Will now put the values into one set.


setA.intersection_update(setB) #Will now only keep the numbers that appear in both sets, removing the differences.
print(setA)

setB.difference_update(setA) #Will remove the values not found in setA.
print(setB)

setA.symmetric_difference_update(setB) #Does not take values found in both sets, instead it takes the remaining values from both sets and creates a new set.
print(setA)


#Advanced

setC = {1,2,3,4,5,6}
setD = {1,2,3}

print(setC.issubset(setD)) #The first set values are all found in the second set, which makes this false.
print(setD.issubset(setC)) #This will print True because only 1,2,3 are found in the other set, but not the rest of the values. (4,5,6)

print(setD.issuperset(setC)) #Complete inverse to the prior method. 

print(setC.isdisjoint(setD)) #Returns false because these set have same elements


#Frozen Set

a=frozenset([1,2,3,4])

#a.remove(2) #This won't work because the list is forzen. You cannot modify it.

print(a)


#Some string shit.

my_string = "Hello World"
print(my_string.replace('World', 'Universe'))

my_list = my_string.split(" ")
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list2 = ['a'] *6
print(my_list2)

my_string2 = ''.join( my_list2)
print(my_string2)


#Format
var = "Tom"
myString = "the variable is %s " % var #We gave a placeholder with a string using %s, then called var to put into myString
print (myString)

var = 3
myString = "the variable is %d " % var #place %d for intergers. Adding decimals here would still print three.
print (myString)

var = 3.1232
myString = "the variable is %f " % var #Gives us a float value. This has six digits by default. Specify using %.2f, this will print out two digits.
print (myString)

#.format
var = "Tom"
var2 = 3.12029
myString = "the variable is {} and {:.2f}".format(var, var2) #Prints string in first {}, and float in second {}
print (myString)

#f-Strings (they look nice)
var = "Bracy"
var2 = 6.12029
myString = f"the variable is {var} and {var2:.2f}" #I think it should be understanding now.
print (myString)