'''
import sk6
#print(dir(sk6))#dir will return all available methods

#print(type(sk6.data))
#print(type(sk6.details))

#always first check the type

#print(sk6.data)
#in above cases we are accesing  via module name

from sk6 import data
print(data)
print(data.keys())

data['marks'] = [44,45,46,77]
print(data)

print(sk6.__doc__) #it returns doc string (description)

#we can use also * to get all methods/attributes
'''
from sk6 import *
print(data)
details('ram','vizag')
