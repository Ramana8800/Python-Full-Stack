'''
Q.Palimdrom number?

Q.Amstrong number?
 
num = int(input("Enter a number:"))
length_ = len(str(num))
amstrong_ = 0
for i in str(num):
    amstrong_ = amstrong_+int(i)**length_
    print(amstrong_)
if amstrong_ == num:
          print(f'{num} is Amstrong Number ')
else:
    print(f'{num} is not Amstrong Number ')



Q. Find the perfect number?

--> perfect number means the sum of factors is equal to number
ex: given 6 --> the factors 1,2,3
1+2+3 = 6

num = int(input("Enter a number:"))
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum = sum+i
if sum == num:  
    print(f'{num} is perfect number')
else:
    print(f'{num} is not perfect number')


Q. Fibanocci number?


num = 0
num_2 = 1
print(num,num_2,end=' ')
for i in range(1,10):
    num_3 = num + num_2
    num = num_2
    num_2 = num_3
    print(num_3,end=' ')



Functions:
---------
--> A function is a block of code that can be excuted onlywhen is called..
--> A function start with def keyword and the line called as definition line,where we can define a function name
--> And if we want to excute the program in the function,need to call with thefunction name define at def line
syntax
------
def fun_name(parameters):
     pass
    fun_name(arguments)

Eg:
def add_(a,b):
   print(a+b)
add_(5,6)

Arguments:
---------
Positional Arguments:
--------------------
--> The arguments should be same at def line and calling,incase if they are not same number will raise an errror

Eg:

def add_(a,b):
    print(a+b)
add_(5,7)

Example for fibonacci series

num = 0
num_2 = 1
def feb_(num,num_2): 
    print(num,num_2,end=' ')
    for i in range(1,10):
      num_3 = num + num_2
      num = num_2
      num_2 = num_3
      return num_3
feb_(num,num_2)

Default arguments:
----------------
--> The default arguments where the function will only consider the data at calling,even though data pressent at def line
Eg:


def data_(a=8,b=9):
    print(a+b)
data_(1,10)
Eg:

def feb_(num,num_2):
    print(num+num_2)
feb_([1,3],[5,6])
Eg:

def prime(num=10,count = 1):
    for i in range(1,num+1):
        if num %i ==0:
            count +=1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
prime(num = int(input("Enter a number:")),count = 0)

keyword arguments:
-----------------
--> keywords arguments are sending arguments in a pair(a=2),and the pass order is not consider

Eg:

def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='teja',age = 23,batch=6,location = "vizag")


Variable lengt argument:
-----------------------

Eg:
    
def all_(*Name):
    print(Name)
all_('teja','garikapati','sony','sai')

Keyword length argument
-----------------------

def Details(**data_):
    print(data_)
Details(Name='Teja',age=23,location = 'vizag',batch =6)

return:
------
--> return key word used inside the function , once the return is excuted means it will get back to calling with return values
eg:
'''
def all_(a,b):
   return a-b
print(all_(7,9))

































































