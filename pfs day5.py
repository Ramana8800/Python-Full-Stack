'''
Indexing
-------
positive--> ng0
negative--> -1


Eg:
   
all_ = [12,[1,'python',[1,4],(78,[6,7]),['java',78]]]
print(all_[1] [3][1])

data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])

Len():
-----
Eg:
    
data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(len(data_[1][3][1]))

sciling:
-----
 eg:

data_ = [1,2,3,4,5,6,7]
print(data_[0:7])

Methods:
--------
append()
-------
--> append methon will add new iteams into list at last index position
syntax-->variable_name.append(iteam)

Eg:
 
go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)
go.append("ram")
print(go)

extend()
-------
--> extend will add the iteams into a list at last index position,but it will give each value as one index inside list
syntax--> variable_name.extend(iteams)
eg:

go = [1,2]
go.extend(("python"))
print(go)

pop:
----
--> remove index value
eg;

m = [1,2,3,4,5]
m.pop(3)
print(m)

remove:
-------
--> remove will delete iteams based on the value given init.
Syntax--> variable_name

Eg:
''' 
m = [5,1,2,3,4,"python"]
m.remove(5)
print(m)





























