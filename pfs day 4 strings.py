'''
Strings
-------
Operations
----------
1.Indexing
----------
--> indexing is used to get a char that you looking to access.
Types:
1.Positive indexing
------------------
positive indexing starts from 0 index
syntax--> print(variable_name[index_position])
eg:
   
text = 'python'
print(text[3])

2.Negetive Index:
----------------
Eg:

text = 'python'
print(text[-1])

len():
----
--> len() is a built-in function that used get number of char present in the string
syntax--> len(variable_name)
eg:

text = 'pythom is a programming language'
print(len(text))

slicing:
-------
--> This is used to access the particular part from the string
Syntax--> variable_name[start:end]
Eg:

txt = 'python is a programming language'
print(txt[12:23])
print(txt[12:])
print(txt[:23])
print(txt[::-1])
print(txt.upper())

Upper()
------
--> Used to convert all small char into cap
Eg:

txt = 'python is a programming language'
print(txt.upper())

Lower()
------
--> Used to convert all caps into small
Eg:

txt = 'Python is a Programming Language'
print(txt.lower())

Index()
------
--> Used to know the index position of an char
syntax--> variable_name.index('substring',start,end)

eg:

txt = 'python is a programming language'
print(txt.index('i',9,18))
print([7])

replace()
--------
--> used to replace old substring into new substring
Eg:
txt = 'python is a programming language'
print(txt.replace(old:'python',new:'java'))

split()
------
--> This method is used to saparate the string based on given substring

 Eg:
 '''
txt = 'python is a programming language'
print(txt.split(' '))
print(txt.count('a',1,12))

c


















    


















