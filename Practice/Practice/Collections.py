#colletions: Counter, namedtuple, OrderedDict, defaultdict, deque

#Counter

from collections import Counter

a = "aaaaaaaaabbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1)) #Gives you the value that is the most common. So if the number is 2, you will be getting c: 3 next. This also returns a list with tuples in it.
print(my_counter.most_common(1)[0][0]) #Will only print a

print(list(my_counter.elements()))

#namedTuple
from collections import namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

#OrderedDict

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

#DefaultDict

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a']) #prints 1
print(d['c']) #prints default value, so in this case 0 since int is the default value that is placed on line one.


from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.popleft()
print(d)

d.extend([4,5,6])
print(d)
d.rotate(1)
print(d)