'''
for loop:
--------
--> for loop is used to iterate over a sequence or iterable datatypes
Eg:

nums = [12,3,4,78]
for num in nums:
    print(num)

Eg:

nums = "python"
for num in nums:
    print(num)

else in for:
-----------
--> unlike if-else,else block in for statements is excuted after completed of all iterations
Eg:
    
nums = "python"
for num in nums:
    print(num)
else:
    print("for ended")

Eg:

nums = [1,2,3,4,"tej",5,8,9,"ram"]
for num in nums:
    print(num)
    if num =="tej":
        break

Eg:


val_ = [1,2,3,4,5,6,7,8,9]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')


break:
------
--> the break used to stop iteration based on the condition given
Eg:

nums = [1,2,34,5,6,7,8,9]
for num in nums:
    if num == 5:
        continue
    print(num)

pass:
----
--> A pass is called as space holder , that is used after statements like (if,for ,else) not to raise any error 

Eg:

for j in range(1,11):
    if j == 15:
        print(j)
    else:
            pass

assert:
-------
--> assert is a key word used to check the condition, incase the condition is false , it will raise the error (AssertionError)
Eg:

age = 15
assert age >= 15 , 'Not eligible to vote'
print('Your eligible to vote')

num = 1
while num<5:
    print(num)
    num +=1
    
Q.print a number is prime?

limit_= int(input("Enter a number:"))
for i in range(2,limit_+1):
     count = 0
     for j in range(1,i+1):
         if i % j == 0:
             count += 1
     if count == 2:
        print(f'{i} is prime')

Q. traingle stars?

star_ = int(input("Enter a number:"))
count = 0
for i in range(1,star_+1):
    for j in range(1,i+1):
        count += 1
        print('*',end=" ")
    print()


Q. Finding vowels in sentance?


words_ = 'Python Is A Programming Language'
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i in vowels:
        count +=1
    
        print(f'{i} is vowel')
print(count)

Q.Remove duplicate values?

digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)
'''
Q.Find out duplicate values in tuple?
   


















































































        

