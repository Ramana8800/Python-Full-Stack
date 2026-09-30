'''
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

BMI Senario --> link with Exception handling with usage of while

while <condition>:
    statement(s)...
    ............


while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in meters:"))
        name = str(input("Enter the name:"))
        if weight > 0 and height > 0:
            #print(weight,height)
            break
        else:
            print("value must be positive")
    except Exception as e:
        print(e)
bmi = (weight)/((height)**2)
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
'''

'''
#file handling -->create files,make some changes over files
#we will open(),with()-->.txt files
#we have different modes-->'r','w','a','r+'

file = open('ram.txt','r')
#print(file)
#now read content from the file
#print(file.read())
#print(file.readline()) #reads a single line from the file
#print(file.readlines())#returns list of lines

#'w' mode --> it automatically creates a new line and if same files existing it overrides

file = open('bheem.txt','w')
print(file)
#print(file.read()) #it is not readble
file.write("PFS 06 and da6 students are good")
file.close()

#we can use 'with'keyword
with open('bheem.txt','w') as file:
    print(file)#in this case we already bheem.txt file the content is overried
#no need for usage of close() content will be directly written
    file.write("PFS 06 and da6 students are good")
    file.write("\nme and you")

data = ['codegnan','python','vizag','pfs']
with open('qw.txt','w') as file:
    #file.write(data) in this case write() fails as it needs only str
    for text in data: #using for loop because data in the list
        file.write(text)

data = ['codegnan','python','vizag','pfs']
with open('asd.txt','w') as file:
    file.writelines(data) # this is directly insert the data from the list
'a':
---
#'a'--> will create a new file,if file is already existing content will be added instead of overring
with open('asd.txt','a')as f:
    f.write("\n Today we are having a webinar related to voiceai agent")

'r+':
----
--> it performs both read and write operarations

with open('asd.txt','r+') as f:
    print(f.read())
    f.write("\n webinar is very important")#in this case it starts writing when we use write() first and then read()
    print(f.read())
'''

with open("marks.txt",'w')











