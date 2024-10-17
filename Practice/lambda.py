# lambda arguements: expression

add10 = lambda x: + 10 #lambda is an input, which is x.
print(add10(5))

def add10_func(x):
    return x + 10

mult = lambda x, y: x*y
print(mult(2,7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) #Sorts the first arguement

print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1]) #List is now sorted in the y index of the list. [(x, y)]
print(points2D_sorted)


def sort_by_x(x):
    return x[0]

points2D_sorted = sorted(points2D, key=sort_by_x)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])


#map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a) #Multiples each value in the a list.
print(list(b))

c = [x*2 for x in a] #Simple way.
print (c)

#filter(func, seq)
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2==0]
print (c)

#reduce(func, seq)
from functools import reduce
a = [1,2,3,4,5,6]

product_a = reduce(lambda x,y: x*y, a) #Will multiply all values in the list. It adds up as the list progresses.
print(product_a)
