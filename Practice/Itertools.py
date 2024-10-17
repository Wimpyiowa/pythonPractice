# intertools: product, permutations, combinations, accumlate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations 
a = [1,2,3]
perm = permutations(a, 2) #Prints all possible orderings. We can also shorten the amount of permutations by adding a value on a second expression
print(list(perm))


from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2) #Second expression is manitory, and in this example, this should print out all combinations with two numbers from the selected list
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) #Replaces the second value
print(list(comb_wr))

from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a) #Will add up numbers as the list goes on.
print(a)
print(list(acc))
acc = accumulate(a, func=operator.mul) #This will multiple numbers as the list goes on. This is only possible with operator imported
print(list(acc))

from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dim', 'age': 25,}, {'name': 'Lisa', 'age': 27}]
group_obj = groupby(persons, key=lambda x: x['age']) #Calls for age, if there are values of the same age, they will be put into the same list. If it's a different value, that value will be put into a different list.
for key, value in group_obj:
    print(key, list(value))


from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3]
#for i in cycle(a):
    #print(i)

for i in repeat(1, 4): #Use the second expression to tell the program how many times you want to run this loop. Otherwise, this prints infinite.
    print(i)