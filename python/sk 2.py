'''
Input Formating:Accept input from user
Integer,float,string,comma separated values,space separated values

#input from user--> input()-->can accept any type--> result is str

name = input("enter the name:")
print(name)
print(type(name))
print(len(name))

#split()

#by default it will be space separated
name = input("enter the name:").split()
print(name)
print(type(name))
print(len(name))


#split(',')--> comma separated values

name = input("enter the name:").split(',')
print(name)
print(type(name))
print(len(name))

#Accept single integer,multiple integer values,group of integers

num_1 = int(input("Enter a number:"))
print(num_1)
print(type(num_1))

#Every built_in datatype is a built-in function-->functions-->objects
#usage of map()--> group of integers

numbers = list(map(int,input("Enter the values:").split(',')))
print(numbers)
print(type(numbers))

#o/p :
#Enter the values:12,13,14
#[12, 13, 14]
#<class 'list'>

#Group of float values

numbers = list(map(float,input("Enter the values:").split(',')))
print(numbers)
print(type(numbers))

#o/p:
#Enter the values:12,13,14
#[12.0, 13.0, 14.0]
#<class 'list'>

#Accept multiple values --> integers

temperature,pressure = map(float,input("Enter the values:").split(','))
print("Temperature is:", temperature)
print("Pressure is :",pressure)


#Exaple Question:

text = input("Enter the secret note:")
with open("secret.txt",'w') as file:
    file.write(text)
with open("secret.txt") as new_file:
    print(new_file.read())  

print()--> output formatting(fstring)

a,b = 13,4.5
print(a,b)#by defualt sep=' '
print(a,b,sep=' ')
print(9,15,sep=':')
print("codegnan","python","vizag",sep='--->')

#end by defualt throws new line,we can modify it..
a,b = 13,4.5
print(a,b,end=' ')
print("codegnan is in vizag",end='\t')
print("pfs6 and da6")
print()
print('------->welcome to the game----->')


#use print() and build a simple calculator application
#ask inputs from user --> add,sub,mult,and divide

a,b = map(int,input("enter the nums:").split(','))
add = a+b
sub = a-b
mul = a*b
divide = a/b
print("---------->calculator-------->")
print("allows only +,-,*,/")
print()
print("addition:",add)
print("subtraction:",sub)
print("multiplication:",mul)
print("division:",divide)
print()

#usage of %d,%f,%s
#print("usage of %"%(args))
price = 45.356; grade = 'A';stock = 15
print("price is %d"%price)#%d stands for int value,%f is float,%s is string value
print("price is %f"%price)#decimal value
print("price is %.f"%price)
print("price is %.1f"%price)
print("grade is %s"%grade)


#Area of circle:
radius = float(input("enter radius:"))
area = 3.1416*radius**2
print("Area is %.2f"%area)


#New style formatting----> fstring
name = "codegnan";batch="pfs6"
print(f'{batch} is in {name}')
print(f'i am in {name}')
print("name is %s"%name)


#control block statements --> they control the flow of the program
#conditional statements(if,elif,else):
------------------------------------
#repetition stetements (loops)(for,while)
#jumping statements (break,continue,pass)

#suntax for conditional statements:

if <condition>:
    statement(s)...
    ............
    ............
elif<condition>:
    statement(s)..
    ..............
else:
    statement(s)...
    ............


#BMI converter (body mass index --> weight,height)(weight kgs,height cms,meters
#height --> feets-->1 feet -->12 inches--> 1 inch -->2.54 cm
#1 feet ---> 30.48 cm --> 0.3 m
#bmi = weight/((height)**2)

weight = int(input("Enter the weight in kgs:"))
height = float(input("Enter the height in meters:"))
name = input("Enter the name:")

if weight > 0 and height > 0:
    bmi = weight/((height)**2)
    
    if bmi<18.5:
        print(f'BMI of {name} is {bmi} amd you are underweight--->Eat well')
    elif bmi>=18.5 and bmi<24.9:
          print(f'BMI of {name} is {bmi} amd you are Healthy--->Keep consistent')
    elif bmi>=25 and bmi <=29.9:
          print(f'BMI of {name} is {bmi} amd you are overweight--->\Eat well')
    elif bmi>30:
          print(f'BMI of {name} is in obese category and bmi is {bmi}')
    
else:
    print("Do enter only positive numbers greater than 0")

#Task --> User can enter height in centimeters,feets--> meters
#cal BMI
#make all user validations for height --> cms,feets

#if the same above BMI scenario we want it to be repeated for specific number of times
#repetition ststements --> for,while
#for keyword--->
#In this case we want 5 iterations to be happened

print("----------BMI Calculation------------")
for i in range(5):
    weight = int(input("Enter the weight in kgs:"))
    height = float(input("Enter the height in meters:"))
    name = input("Enter the name:")

    if weight > 0 and height > 0:
        bmi = weight/((height)**2)
        
        if bmi<18.5:
            print(f'BMI of {name} is {bmi} amd you are underweight--->Eat well')
        elif bmi>=18.5 and bmi<24.9:
              print(f'BMI of {name} is {bmi} amd you are Healthy--->Keep consistent')
        elif bmi>=25 and bmi <=29.9:
              print(f'BMI of {name} is {bmi} amd you are overweight--->\Eat well')
        elif bmi>30:
              print(f'BMI of {name} is in obese category and bmi is {bmi}')
        
    else:
        print("Do enter only positive numbers greater than 0")

print("----------BMI Calculation------------")
details = {'names':[],
           'weights':[],
           'heights':[]}
n = int(input("Enter how many times you want to repeat:"))
for i in range(n):
    name = input("Enter the name:")
    details['names'].append(name)
    weight = int(input("Enter the weight:"))
    details['weights'].append(weight)
    height = float(input("Enter the height:"))
    details['heights'].append(height)
    
    if weight > 0 and height > 0:
        bmi = weight/((height)**2)
        
        if bmi<18.5:
            print(f'BMI of {name} is {bmi} amd you are underweight--->Eat well')
        elif bmi>=18.5 and bmi<24.9:
              print(f'BMI of {name} is {bmi} amd you are Healthy--->Keep consistent')
        elif bmi>=25 and bmi <=29.9:
              print(f'BMI of {name} is {bmi} amd you are overweight--->\Eat well')
        elif bmi>30:
              print(f'BMI of {name} is in obese category and bmi is {bmi}')
        
    else:
        print("Do enter only positive numbers greater than 0")

print(details)


#Exception handling:
-------------------
#Exception handling is a mechanism to a program which responds to run time error or compilation
#Exception-->It tries to make our program go in a normal flow
#key words--> try,except,finally
#for every try except is mandatory..
#simple scenario to understand the exception
a,b = map(int,input("Enter the values:").split(','))
try:
    result = a/b
    print(result)
except Exception as e:
    print("find it")
    print(e)

#same above case accept inputs in try block
    
try:
    a,b = map(int,input("Enter the values:").split(','))
    result = a/b
    print(result)
except Exception as e:
    print("find it")
    print(e)

#In above case we will get Valueerror,ZeroDivisionError....
#Possible type of errors --> TypeError,ValueError,NameError,IndexError,AttributeError,ArthmeticError...
    
try:
    a,b = map(int,input("Enter the values:").split(','))
    result = a/b
    print(result)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("make sure to give denominator greater than zero")

except AttributeError:
    print("please check the methods/function name properly")
except NameError:
    print("please first understand the syntax and be good at spellings")
finally:
    print("Its done now you have understand exception handling")


#Student Grade checker:
for i in range(5):
    marks = int(input("Enter the marks:"))
    if marks <0 or marks>100:
        print("Invalid marks entered")

    elif marks >=90:
      print("Grade: A")
      print("Remark: Outstanding")
        
    elif  marks >=80 and marks<=89:
      print("Grade: B")
      print("Remark: Excellent")
        
    elif  marks >=70 and marks<=79:
      print("Grade: C")
      print("Remark: Good")
        
    elif  marks >=60 and marks<=69:
      print("Grade: D")
      print("Remark: Fair, needs improvement")

    elif  marks>=50 and marks<=59:
      print("Grade: E")
      print("Remark: Poor, needs serious improvement")
    else:
      print("Grade: F")
      print("Remark: Failed, needs to reappear")


#Even or Odd
for i in range(5):
    num = int(input("Enter the number:"))
    if num ==0:
        print("Zero is neither even nor odd")
    elif num%2 ==0 and num>0:
        print("Number is even")
    elif num%2==0 and num<0:
        print("num is negetive even")
    elif num%2!=0 and num>0:
        print("Number is odd")
    
        
    else :
        print("Number is negetive odd")
'''
#Season Identifier:
for i in range(5):
    month = int(input("Enter the month:"))
    if month <=0 or month>12:
        print("Invalid month entered")
    elif month==12 or month ==1 or month ==2:
        print("Season:Winter")

    elif month==3 or month ==4 or month ==5:
        print("Season:Spring")

    elif month==6 or month ==7 or month ==8:
        print("Season:Summer")

    else:
        
        print("Season:Autumn")


































