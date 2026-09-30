#functions:

#positional arguments,keyword arguments,default arguments
'''

def add(a,b):
    return a+b
print(add(5,6))
print(add("codegnan","python"))
print(add([1,2,3],[4,5,6]))
c,d = map(int,input("Enter the values:").split(','))
print(add(c,d))

#keyword arguments-->name of the arguments should match

def grocery(iteam,price):
    key word arguments usage
    print(f'Iteam is {iteam}')
    print(f'Price is {price}')
grocery("milk",35)
print(grocery(price=44,iteam="Bread"))#it is also returns None as nothing to be printed
#grocery("jam",100,2) #in this case positional arguments fails as we have only 2 arguments in function definition

#default arguments -->we can make any number of arguments as default


#def grocery(iteam,price=30):
#def grocery(iteam = "milk",price): raise Error
def grocery(iteam='jam',price=50):
    print(f'Iteam is {iteam}')
    print(f'Price is {price}')
grocery("milk",35)
print(price=44)

#Usage of variables like global and local variables:

count = 10 #global variable
def details():
    count = 15 #local variable
    print(f'value of count is {count} inside the function')
    count= count+5
    print(count)
details()


#uasge of global keyword

count = 10#global variable
def details():
    global count
    count = count+15
    print(f'value of count is {count} inside the function')
details()
print(f'value of count is {count}out side the function')


#Enclousing Scope --> nested function

def outer():
    #nested functions
    count = 5
    def inner():
        #inner function to use count variable
        nonlocal count
        count = count*4
        print(f'value of count is {count}')
    inner()
    print(f'value of count is {count} outside')
outer()

#built-in scope --> usage of built-in functions as variables
len =13
print(len)

a =['codegnan','python','data']
print(len(a))#raises typeError as we have used len() somewhere

#LEBG rule --> local,enclosing,built-in,global
#Built-in functions,anonymous,functions,recursive functions

#print(dir(__builtins__))
#print(abs(-23)) #returns the absolute value
#Empty values are --> None,' ' ,0,False,(),{}
#all,any()
x=[23,34,'poll']
x.append(None)
#print(x)
#print(all(x))#all(iterable) it needs all values in the iterable to be exists
#print(any(x))#any(iterable) it needs any one value to be present

print(bin(12))

print(chr(67))#returns the concerned object(chr)
print(ord('A')#returns the ASCII value for any character,symbol
print(divmod(6,2)#perform 6//2(quotient) --> 6%2(reminder)-0
print(pow(4,2))#base,exponent

print(round(5.345))
print(round(5.345,2))#digits to be rounded off


def rectangle(l,b):
    #area of rectangle
    return l*b
print(rectangle(7,4))
print('Area of rectangle:',rectangle)

#social media user login user first name last name--->full name

fname,lname = input('Enter the names:').split(',')
#print(fname,lname)
full_name,last_name = lambda fname,lname:fname.title().strip()+" "+lname.title().strip()
print(full_name(fname,lname))

#Accepting input from user and find even or odd

n = int(input("Enter the number:"))
result = lambda n :"Even" if n%2==0 else "odd"
result1 = lambda n :n**2 if n%2==0 else n**3
print(result(n))
print("New result is :",result1(n))

#filter(),map(),reduce()

#filter():-->we want to  specific filtered result

data = [1,3,45,24,12,36,3]
#filter only even numbers from list
new_data = list(filter(lambda x:x%2==0,data))
print(new_data)

#Try above usng user defined function with  for loop..

data = [1,2,45,24,12,36,3]
def final(data):
    #filter values
    new_data = []
    for i in data:
        if i %2==0:
            new_data.append(i)
    return new_data
print(final(data))


#filter disired names from the list
names = ['saketh','ram','python','akash','neha']
new_names = list(filter(lambda i:len(i)>=6,names))
print(new_names)

map():
---
it will apply logic for each value (google maps)

lst =list(map(int,input("Enter the values:").split(',')))
print(lst)
data = [1,3,4,5]
print(data)
final = list(map(lambda x,y:x+y,lst,data))
print(final)

EX:

prices = [2000,2500,1500,4500,3000]
#discount of 10% for every price
disc_prices = list(map(lambda price:(price-price*0.1),prices))
print(disc_prices)


#reduce-->functool
#reduce()--> it will check for logic and make it to a single value

import functools
from functools import reduce
result = reduce(lambda x,y:x*y,[12,3,5,6])
print(result)
f = reduce(lambda x,y:x+y,[12,3,5,6])
print(f)

#task:try above two cases using functions

#Recursive functions : A function can call itself
#factorial ,Fibonacci,sum of numbers...
#Recursive functions --> Because (it tells when to stop the recursion)
                     --> Recursive case (it tells how to start recursion)

syntax:
-----
def func():
    if base:#base case
        return
    func() #recursive case
func()

'''
#let's link above case to factorial
#5!-->5*(5-1)*(5-2)*(5-3)*(5-4)*1

n= int(input("Enter the value:"))
def fact(n):
    #factorial
    if n==0 or n==1:
        return 1
    elif n<0:
        return "input must be greater than 1"
    else:
        return n*fact(n-1)
print(fact(n))










