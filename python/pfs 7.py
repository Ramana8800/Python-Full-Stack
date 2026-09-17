'''
union()
------
--> the union() will combine two set into a single set
syntX --> set_1.union(set_2) or set_1|set_2
eg:

data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.union(nums))
print(data_|nums)

--> this will gives us the common elements from both sets
syntax -->

eg:

data = {1,2,3,4}
nums = {4,5,6}
print(data.intersection(nums)
print(


difference()
-----------
--> it will display the different elements from set_1,but not the set_2 elements
sytntax --> set_1.difference(set_2) or set_1-set_2

eg:
--
data = {1,2,3,4}
nums = {4,5,6}
print(nums-data)
print(nums.difference(data))

symmetric_difference():
----------------------
--> different elements from the both

syntax--> set_1.symmetric_difference(set_2) or set_1 ^ set_2

eg:

data = {1,2,3,4}
nums = {4,5,6}
print(nums^data)
print(data.symmetric_difference(nums))

Methods:
-------

add()
-----
--> add() method will add only one element at a time
syntax--> set.add(element)
eg:

data = {1,2,3,4}
print(data)
data.add(7)
print(data)

Update():
---------

--> we can add more one elements by using update method
syntax--> set.

Eg:
    
data = {1,2,3,4}
nums = {4,5,6}
print(data)
data.update([8,9])
print(data)
data.update(nums)
print(data)

REmove():
-------
--> remove() method will del the given element from the set
-->  if the element is not present in the set, it will rise the error


data = {1,2,3,4,5}
data.remove(3)
print(data)
data.remove(5)
print(data)

Discard():
---------
--> The metod is used to del the elements from the set , but never raise any error even the element not inside set
syntax--> se.discard(element)

eg:

data = {1,2,3,4}
data.discard(7)
print(data)
data.discard(1)
print(data)
'''
clear():
-------
--> the method is used to del all elements from the set and it will written empty s
syntax--> se.clear()
data ={1,2,3,4}
print(data)
data.clear()
print(data)





























































