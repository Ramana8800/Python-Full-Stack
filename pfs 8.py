'''
Accessing:
----------
--> dict can access by calling key,we will get value from that key
syntax-->dict['key']

get():
-----
--> get() method is also used to get the value from

Update():
--------
-->Method is used to update a key,incase if the key is not present inside dict then it add that key:value
syntax-->dict.update({key:value})
-->There is another way to update akey
syntax--> dict[key] = value
Eg:

data_ = {'name':'Teja','balance':7000,'Adr':123454321,'PANC':'GPXT379Y',2:[3,4]}
print(data_['Adr'])
print(data_.get(2))
print(data_)
data_['name'] = 'sony'
data_[2] = [1,2]
data_['AC'] = 123456
data_.update({'name':'ram'})
data_.update({'ATMPIN':1234})
print(data_)

values():
-------
-->values() method is used to get all the values in the dict
eg:

data_ = {'name':'Teja','balance':7000,'Adr':123454321,'PANC':'GPXT379Y',2:[3,4]}
print(data_.values())

keys():
------
--> keys() method is used to get all the keys in the dict
Eg:

data_ = {'name':'Teja','balance':7000,'Adr':123454321,'PANC':'GPXT379Y',2:[3,4]}
print(data_.keys())

items():
-------
--> The method will get the key:value separated from the dict
syntax-->dict.items()
Eg:
data_ = {'name':'Teja','balance':7000,'Adr':123454321,'PANC':'GPXT379Y',2:[3,4]}
print(data_.items())

clear():
-------
--> clear() method is used to del all data from dict
syntax-->dict.clear()

Eg:

data_ = {'name':'Teja','balance':7000,'Adr':123454321,'PANC':'GPXT379Y',2:[3,4]}
print(data_)
del data_['Adr']
print(data_)
data_.clear()
print(data_)


if statement:
-------------
--> if condition become true,then it will execute inside block of code
--> incase it becomes false,then it will never entry inside block

Eg:

age = 15
if age>=18:
  print("Elegible to vote")

age = 19
if age>=18:
    print("Elegible to vote")


a= 90
b= 78
if a>b:
    print(a)


if-else:
-------
--> else for if ststement is a fall-back statement,incase if condition is false then else block will excute
Eg:

age = 15
if age>=18:
    print(f'your {age} Eligible to vote')
else:
    print(f'your {age} you have to wait {18-age}')

a = 90
b = 780
if a>b:
    print(a)
else:
    print(b)


elif:
-----
--> elif statement is used to check more possible outcoms

eg:

a = 90
b = 780
c = 670
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

Eg:
    
num = 7
num_2 = 3
user_opt = int(input("Enter \n1.add \n2.sub \n3.mul \n4.pow:"))
if user_opt ==1:
    print(num + num_2)
elif user_opt ==2:
    print(num - num_2)
elif user_opt ==3:
    print(num * num_2)
else:
    print(num**num_2)

nested if
---------
--> if inside an if statement is called nested if

eg:

app_details = {"pin":1234}
import random
user_pass = int(input("Enter your app passoward:"))
otp = random.randint(1000,9999)
if user_pass == app_details["pin"]:
    print("password is correct")
    print(otp)
    user_otp = int(input("Enter 4 digit OTP:"))
    if user_otp == otp:
        print("welcome to the app")
    else:
         print("incorrect OTP")
else:
    print("password is incorrect")
    
eg:

a= int(input("Enter a number:"))
if a % 2 == 0:
   print(f'{a} is even')
else:
  print(f'{a} is odd:')

eg:
'''
marks_ = int(input("Enter your marks:"))
if marks_>=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_>=70:
    print("B+")
elif marks_>=60:
    print("B")
elif marks_>=50:
    print("c+")
elif marks_>=40:
    print("Fail")























    


































    
  






























