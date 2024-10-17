org = 5
cpy = org
cpy = 6
print(cpy, org)

#Shallow copying
import copy

org = [0, 1,3,4,]
cpy = org.copy() #Method 1
cpy = copy.copy(org) #Method 2
cpy[0] = -10
print(cpy)
print(org)

#Nested, deep copy.
org = [[0, 1,3,4], [5,6,7,8]]
cpy = copy.deepcopy(org) #Method 2
cpy[0][1] = -10
print(cpy)
print(org)

#Custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 27)
p2 = copy.copy(p1)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)

p2.age = 28
print(p2.age)
print(p1.age)