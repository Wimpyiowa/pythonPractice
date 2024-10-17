"""
- The difference between arguements and parameters
- Positional and keyword arguements
- Default arguements
- Variable-length arguements(*args and **kwargs)
- Container unpacking into function arguements
- Local vs. global arguements
- Parameter passing (by value or by reference?)
"""

#arguements and parameters
def print_name(name):
    print(name)

print_name('Alex')

#Postional and keyword
def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)

#keyword
foo(c=1, b=2, a=3) #The order is not important with keywords.

#both
foo(1, b=2, c=3) #Cannot use postional after using a keyword arguement.

def foo1(a, b, c, d=4):
    print(a, b, c, d)

foo1(1, 2, 3)

#Variable Length Arguements
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six = 6)

#forced keyword arguements
def foo(a, b, *, c, d): #Keyword arguements have to be used after b since * is placed
    print(a, b, c, d)

foo(1, 2, c=3, d=4) #Cannot use positional after b(2)

def foo1(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo1(1, 2, 3, last= 100)

#Unpacking arguements
def foo(a, b, c):
    print(a, b, c)

my_list = [0,1,2] #Adding more values will raise an error.
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c':3} #Must be the same length as the function
foo(**my_dict)

#Local vs Global
def foo():
    x = number
    #number = 3 #Creates a local variable
    print('number inside function:', x)

number = 0 #Global variable
foo()

def foo():
    global number #Will make this variable global always
    x = number
    number = 3 
    print('number inside function:', x)

number = 0 #Global variable
foo()
print(number)

#Parameter Passing (R.I.P)
def foo(x):
    x = 5 #local variable (lives inside the function)

var = 10 #Immutable (cannot be changed)
foo(var)
print(var)

def foo(a_list):
    a_list = [200, 300, 400] #Local variable
    a_list += [200, 300, 400] #This will change the list if append is not in the function
    a_list.append(4) #Immutable objects can be modified within a function
    a_list[0] = -100

def foo1(a_list):
    a_list += [200, 300, 400]

my_list = [1, 2, 3] #Values within this object are mutable
foo(my_list)
foo1(my_list)
print(my_list)