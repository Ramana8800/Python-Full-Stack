'''
Expection handling:


try:
---
-->the try block,where we can write code with may contain error
syntax-->
try:
    code lines

except:
-------
--> This will handle error that are raised at try block
syntax--> except ErrorName:
    print("ErrorName")

else:
-----
--> The else block will only excute, if no error at try block
Eg:
try:
    print(num)
    print(5/0)
   
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')


finally
-------
Eg:
try:
    print(num)
    print(5/0)
   
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
finally:
    print('End')

File Handling
-------------
--> The file handler is a object , which is used to create,update,read,and delete...
modes:
r--> thr (r) mode is used when the read() function is used
Eg:
with open('Example.py','r')as file:
    print(file.read())

w-->
Eg:
with open('Example.py','w')as file:
        file.write('this is example')

a-->
'''

with open('Example.py','a')as file:
        file.write('this is example')























    
