'''
for<temp> in range(obj):
   ststement(s)...

Nested Loops-->(for in for) --> these are primarily used for pattern printing

syntax:
for i in range(outer_loop_range):
    for j in range(inner_loop_range):

    #code block

for i in range(3):#0,1,2
    for j in range(2):#0,1
        print(f'i={i},j={j}')

# In above case for complete j value of 0 i value will be 0,1,2 and follows same for others

for i in range(3):
    for j in range(3):
      print(i,j,end=" ")# Now entire result will be in one single line
      print("python")
   # print("codegnan")
    print()#only when inner loops is complete before starting outer


for i in range(2):#0,1
    for j in range(i):#first i value will be 0 loop does not start for j
        print(f'i={i},j={j}')


for i in range(3):#0,1,2
    for j in range(i+1):#first i value will be 0 loop does not start for j
        print(f'i={i},j={j}')


for i in range(3):#0,1,2
    for j in range(i-1):#as here for i=0,j becomes -ve ,i=1 j becomes 0
        print(f'i={i},j={j}')

#Now lets link above to patterns

#Square pattern

for i in range(3):#0,1,2
    for j in range(3):
        print("*",end=" ")
    print()


#rectangle pattern

for i in range(3):#0,1,2
    for j in range(4):
        print("*",end=" ")
    print()


#Number based patterns-->row wised,column wised...

for i in range(5):
    for j in range(4):
        print(j+1,end=" ")
    print()

#Now keeping both start and end vlues

for i in range(1,4):
    for j in range(1,5):
        print(j,end=" ")
    print()



for i in range(4):                      
    for j in range(4):
        print(i+1,end=" ")
    print()


for i in range(4):
    for j in range(4):
        print(i+1,end=" ")
    print()

----------------*-----------------
num = 1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num+=1
    print()

o/p:
1 2 3 
4 5 6 
7 8 9 

----------------*----------------
for i in range(3):
    for j in range(65,69):
     print(chr(j),end=" ")
    print()

o/p:
A B C D 
A B C D 
A B C D 
-----------*---------------
for i in range(65,69):
    for j in range(3):
     print(chr(i),end=" ")
    print()


o/p:
A A A 
B B B 
C C C 
D D D 

--------------*-------------------

for i in range(5):
    for j in range(5-i):
        print('*',end="  ")
    print()

o/p:
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*
--------------*--------------
num = 1
for i in range(4):
    for j in range(i+1):
     print(num,end=" ")
     num +=1
     
    print()

o/p:
1
2 3
4 5 6
7 8 9 10
---------*-----------

num = 1
for i in range(4):
    for j in range(i+1):
     print(num,end=" ")
    print()

o/p:
1 
1 1 
1 1 1 
1 1 1 1 

'''
num = 1
for i in range(4):
   for j in range(i+1):
       print(num,end=" ")
       #num +=1 
   print()
               














































