#multiplication

result = 5 * 5
print(result)

result = 2 ** 9 #power
print(result)

zeros = [0, 2] * 10
print(zeros)

zeros = "AB" * 10
print(zeros)

#args, kwargs
def foo(a, b, *args, **kwargs): #kwargs will always be a tuple
    print(a, b)
    for arg in args: 
        print(arg)
    for key in kwargs: #kwargs is a dictionary
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six = 7)

#unpicking containers

numbers = [1,2,3,4,5,6,7]
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

#merged list
my_tuple = (1,2,3)
my_list = [4,5,6]

new_list = [*my_tuple, *my_list]
print(new_list)

#This works with dictionaries as well, but to merge them, you need to place two asterisks in a call
