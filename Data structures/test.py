# # LIST - ORDERED, DYNAMIC MEMORY - XOTIRA KO'P JOY
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# # 2
# fruits.count('tangerine')
# # 0
# fruits.index('banana')
# # 3
# fruits.index('banana', 4)
# fruits.reverse()
# # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruits.append('grape')
# # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# fruits.pop()
# # 'pear'


# # STACK
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# # [3, 4, 5, 6, 7]
# stack.pop()
# # 7
# stack
# # [3, 4, 5, 6]
# stack.pop()
# # 6
# stack.pop()
# # 5


# # QUEUE
# # import collections
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves
# # 'Eric'
# queue.popleft()                 # The second to arrive now leaves
# # 'John'
# # queue                           # Remaining queue in order of arrival
# # deque(['Michael', 'Terry', 'Graham'])


# # LIST COMPREHENSION

# squares = []
# for x in range(10):
#     squares.append(x**2)


# squares = list([x**2 for x in range(10)])
# # [1,4,9,16,..]

# # TUPLE - ORDERED, LIST DAN TEZROQ, KAM XOTIRA, STATIC, O'ZGARMAYDI,immutable

# t = (12345, 54321, 'hello!')
# t[0]
# # Tuples may be nested:
# u = (t, (1, 2, 3, 4, 5))


# # Tuples are immutable:
# # t[0] = 88888


# # but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])


# empty = (1)  # TUPLE EMAS
# print(type(empty))
# singleton = 'hello',
# print(type(singleton))


# SETS - unordered
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
# True
'crabgrass' in basket
# False

    

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
# {'r', 'd', 'b'}
a | b                              # letters in a or b or both OR
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b AND
# {'a', 'c'}
a ^ b                               # letters in a or b but not both XOR
# {'r', 'd', 'b', 'm', 'z', 'l'}



# FROZEN SET
vowels = frozenset({"a", "e", "i", "o", "u"})
vowels.add("p")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'






# DICT ( DICTIONARY ) - UNORDERED,  hashable (STR, INT, FLOAT, BOOLEAN, Class Object, Function object, Tuple) 
# O(1) 
tel = {"jack": 4098, 'sape': 4139}
tel['jack']
# 4098
tel['guido'] = 4127
tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
# 4098
del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
# ['guido', 'irv', 'jack']
'guido' in tel
# True
'jack' not in tel
# False

# ORDERED DICT
import collections
d = collections.OrderedDict(one=1, two=2, three=3)

d
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])

d["four"] = 4
d
# OrderedDict([('one', 1), ('two', 2),
#              ('three', 3), ('four', 4)])

d.keys()
# odict_keys(['one', 'two', 'three', 'four'])



# NAMED TUPLE

from collections import namedtuple
Car = namedtuple("Car" , "color mileage automatic")
car1 = Car("red", 3812.4, True)

# Instances have a nice repr:
car1
# Car(color="red", mileage=3812.4, automatic=True)

# Accessing fields:
car1.mileage
# 3812.4

# Fields are immtuable:
car1.mileage = 12
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

car1.windshield = "broken"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Car' object has no attribute 'windshield'
