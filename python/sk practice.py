'''

#TOken -->keywords,operators,punctuators [],(),{}

batch = ['pfs-6','da-6']
print(batch)
print(type(batch)) #everything is an object(POP-->OOP)
#len()--> returns the number of items in a collection
print(len(batch))
#add 3 more students into list
#list--> collection --> append(),extend(),insert()
batch.append('jfs-6')# append take only one argument
print(batch)
batch.extend(('ram','bheem'))
print(batch)
batch.insert(0,'sai')#inserts given value at specific index
print(batch)

batch.insert(-1,'vamsi')
print(batch)

print(len(batch))
#indexing-->[]--> index starts at 0 and ends at len(obj)-1
print(batch[0])
#print(batch[10]) #Index error --> length is only 7 we are accesing extra
#slicing--> group of values [start:end]
print(batch[:3])
print(batch[4:6])
print(batch[4:])
#last 3 elements --> we prefer negative index values
print(batch[-3:])
print(batch[:3])
print(batch[:-3])
#striding --> [start:end:step]


print(batch[::2])
print(batch[::3])
print(batch[1:5:2])
print(batch[7::4])
print(batch[-1:-4:-1])

#lets include tuple in the above list(tuples are immutable)
batch.insert(2,("vizag","hyd","vijayada"))
print(batch)

print(len(batch[2]))
print(batch[2][:2])
print(batch[2][1])
print(batch[2][::2])#returns (vizag,vij)
print(batch[2].index("hyd"))
#in the tuple we have work on only count() and index()
#index--> first occurance
#count--> returns the count of objects
print(batch[2].count("codegnan"))#returns count as 0
#index will raise error,where as count wii return 0

batch.insert(3,["pfs","da","jfs"])
print(batch)
#now let us apply some of list functions in above batch list
print(batch[3])
print(batch[3][1])
#to convert upper case
batch[3][2] = batch[3][2].upper()
print(batch[3][2])
#now we append to new in batch[3]
batch[3].append("AAA")
print(batch[3])
print(batch)
batch.remove("vamsi")
print(batch)
#remove--> value,POP--> index value
batch.pop()#pop by defualt removes last index value
print(batch)
#batch[2].remove("hyd")#raises attributeError
#del batch[2][1]#tuple is immutable so we can't insert/remove
#we want to remove entire data but keep the list as it is --> clear()
batch.clear()
print(batch)

'''
#lets work on Dictionaries
#dict-->{key:value},keys must be unique
#keys can be int,float,string,list

details = {}
print(len(details))
details['batch'] = ['pfs6']
print(details)
details['course'] = ['python']
print(len(details))
print(details)
details['students'] = ['sai','ram']
print(details)
#we want to update the dictionary
details.update({'branch':('hyd','vizag'),
                'subjects':{'python','Aptitude','Softskills'}})
print(details)

print(details.keys())#return only keys
details['batch'].extend(['jfs','da'])
print(details)
details['students'].extend(['Vamsi','sana','akash'])
print(details)
details['subjects'].add('DSA')#set is unique and unordered
print(details)

#Task--> dtails --> list,set,diction (use codegnan portal as example)
#exams,mock interviews,project demos
#push to github--> share your link in whatsapp group























#
