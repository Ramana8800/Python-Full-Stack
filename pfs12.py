'''
modules:
--> a module ia a python (.py) file that written using functions,variables,operators,etc..
Eg:

import math
print(math.add(2,3))

1.built-in modules:
------------------
-->The modules are develop by the programmers and those comes with installation
Eg:
a.math:
------
Eg:
import math
print(math.add(2,3))

b.os:
-----
Eg:
import os
print(os.getcwd())

c.sys:
------

import sys
print(sys.path)
print(sys.vesion)
print(sys.path)

d.random:
----------

import random
print(random.randint(1000,9999))

2.User-defined modules:
------------------------
importing specific function from the module
--> from module import function
Eg:

from Example import add_,sub
print(add_(90,7))
print(sub(90,7))


import Example as ex
print(ex.add_(90,7))

math
----

import math
print(math.pi)
print(math.ceil(4,3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

Random
-------
import random
print(random.randint(10000,99999))
print(random.randrange(1,100))
color = ['red','blue','green','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

platform
---------

import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

collections
-----------

import collections
data_ = ['banana','apple','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())


from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('taja')

from detetime import detetime

from datetime import datetime
today = datetime.today()
print(today)
print(today.month)
print(today.day)
print(today.year)
print(today.day)
print(today.hour)
print(today.minute)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H-%M-%S'))
print(now.strftime('%d'))


Example program1:
    
import random
attep_ = 3
num = random.randrange(1,100)
print(num)
while attep_ > 0:
    game_ = int(input('Enter a number between 1 and 100:'))
    if game_ == num:
        print("Your guess is correct")
        break
    else:
        attep_ -= 1
        print("your guess is incorrect")


import random
attep_ = 3
num = random.randrange(1,100)
print(num)
while attep_ > 0:
    game_ = int(input('Enter a number between 1 and 100:'))
    if game_ == num:
        print("Your guess is correct")
        break
    else:
        attep_ -= 1
if attep_ == 3:
        print("price money is 500")
elif attep_ == 2:
    print("price money is 200")
elif attep_ == 1:
    print("price money is 100")
else:
    print("Better luck next time")

'''
import itertools
n = itertools.chain([1,2,3],[4,5,6])
print(list(n))














