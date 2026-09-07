'''
Scope of variables:
------------------
1.Local variable
----------------
---> A variable is define inside the function call it as local variable,where the variable can only access with in that function
Eg:

def display():
    name = "Teja"
    print(name)
display()
print(name)

2.Global variable:
-----------------
--> A variable that is defined out side the function call and it can be access anywhere through out program
Eg:

a = 90
def display():
    print(a)
display()
print(a)

Eg:

a = 90
print(a)
def display():
  global a
  a = 10
display()
print(a)

Global keyword:
--------------
--> global is keyword used to reaccess new values to variable that was already define outside the function call
Eg:
a =90
print(a)
def display():
    global a
    a = 10
display()
print(a)

Recursive function:
-------------------
--> The function call itself untill the base condition met..

def Fac(a):
    if a == 0 or a ==1:
        return a
    return a * Fac (a-1)
print(Fac(5))

Lambda function:
--------------
Eg:

add_ = lambda a,b,c : a+b+c
print(add_(10,20,9))

Find cube using lambda function:
    
cube_ = lambda num : num**3
print(cube_(11))

filter():
-------
--> filter() function will perform only on selected elements of iterables
Eg:
    
nums = [1,2,3,4,5]
data_ = filter(lambda a: a%2==0,nums)
print(tuple(data_))

map()
-----
--> map() function will perform on all elements of a iterable
Syntax--> map(lambda arguments : expression,iterable)
Eg:

nums = [1,2,3,4,5]
get_ = map(lambda a: a%2==0,nums)
print(tuple(get_))

reduce()
--> the reduce() function repeatedly applies a function to the elements and reduces them to one final value.
--> It is available in the functools module.
syntax--> reduce(lambda arguments:expression,iterable)
Eg:

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)

List comprehension:
------------------
--> List comprehension is the short form of syntax to creat a list
 syntax 1--> [expression loop condition]
 syntax 2--> [expression condition else loop]
Eg:

old_  = "python"
new_ = [i for i in old_]
print(new_)
Eg2:

old = [1,2,3,4,5]
new = [i for i in old if i%2==0]
print(new)

nested comprehension
--------------------
--> using list comprehension generating list inside list
Eg1:

any = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any)

Eg2:

data_ = [[1,2,3],
        [4,5,6],
        [7,8,9]]       
a = [num for i in data_ for num in data_]
print(a)

generator:
----------
--> generator is a special function which generate one value at atime
'''
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))



























































 
