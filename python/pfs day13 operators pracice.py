'''
#price = 5000#check the type(price)
#accessing input from the user


price = int(input("Enter the price:"))
#discount = 0.1#type(discount)
discount = float(input("Enter discount between 0.1 to 0.2:"))
gst = 0.18
final_price = (price-(price*discount))
final_price = final_price+(final_price*gst)
print("final price is:",final_price)

#operators-->Arithmetic,Assignment,comparision,membership,logical,identity,bitwise...
#Assignment--> = (assigning), +=(update the value)
price = 2500
#New price adding 500
price += 500 #price = price+500#price +=500
print(price)

#comparision--> Compare the values <,>,<=,>=,==,!=

#membership--> in ,not in --> checks for the values in a collecction

#we will have diff prices--> fiff fiscount--> gst same




prices = [15000,2000,13000,25000,35000]
discount = 0.1
discount_2 = 0.15
final_prices = []
#price<= 15000 10%
#price>5000--> to apply adiscunt
#price>20000--> 15%
#get the final prices in a list

for price in prices:
    #print(price)
    if price <=15000 and price > 5000:
        price = (price-price*discount)
        final_prices.append(int(price))
    elif price > 20000:
        price = price - (price*discount_2)
        final_prices.append(int(price))
    elif price < 5000:
        final_prices.append(price)
print(final_prices)

 
#Question1:

marks = []
for i in range(3):
    mark = int(input("Enter marks:"))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
#Requirement 5: Use a condition to check for 75, then remove it using remove()
if 75 in marks:
    marks.remove(75)
#Requirement 6: Remove the final mark using pop() and display the removed value. 
removed_mark = marks.pop()
print("Removed mark:",removed_mark)
print("Final_marks:",marks)
#Requirement 7: Display the final list and its length using len(). 
print("Length of list:", len(marks))

#Question2:

numbers = [20, 10, 30, 20, 40, 20]
#Requirement 1: Sort the list in ascending order using sort()
numbers.sort()
print(numbers)
#Requirement 2: Reverse the sorted list to produce descending order using reverse(),and #descending order:
numbers.reverse()
print(numbers)
#Requirement 3: Ask the user to enter a number to search for.
number = int(input("Enter a number:"))
#Requirement 5: If found, display its count and first index using count() and index(). 
if number in numbers:
       print("count is",numbers.count(number))
       print("first index is",numbers.index(number))
else:
    print("number is not found")
#Requirement 6: Display the smallest value, largest value, and total using min(), max(), and sum()
print("smallest value is:",min(numbers))
print("largest value is:",max(numbers))
print("sum of values in list is:",sum(numbers))

#Question3:
'''
numbers = [10, 15, 20, 25, 30, 35]
#Requirement 1: Create two empty lists named even and odd.
even =[]
odd = []
#Requirement 2: Use a loop to examine every number in the original list.
#Requirement 3: Use a condition with the remainder operator (%) to identify even and odd numbers.
#Requirement 4: Add each number to the correct list using append(). 
for i in numbers:
    if i %2 == 0:
        #print("Even number:",i)
        even.append(i)
       
    else:
        #print("odd number:",i)
        odd.append(i)

#Requirement 5: Use slicing to display the first three and last three values.
print("first three:",numbers[:3])
print("last three:",numbers[-3:])
#Requirement 6: Create a backup of the original list using copy().
Backup = numbers.copy()
print(f'Backup of original :{Backup}')

#Requirement 7: Empty the original list using clear(), then display both the original and backup lists.
numbers.clear()
print(numbers)















    
  
            
        
