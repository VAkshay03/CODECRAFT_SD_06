#SETS

#a set is a collection is unordered, andd unindex
'''important points in sets'''
#1.set items are unordered and does not allows duplicate elements
#2.unordered means that the set doesnt have the particular order
#3.set items dont have index or key
#4.a set is created in the form of the curly braces{}seperated by the , or by using the built-in set() function
#5.it can have any number of items and they may be different types(integer,float,tuple,string etc)
#6.a set donot have the mutable elements like lists,dictionaries,as its elements

sunny=set({1,2,3})
print(type(sunny))#give class <set>
print(sunny)
raj={1,2,2,4,5,6,7,8}
print(raj)#set will not take the duplicates
#it prints {1,2,4,5,6,7,8}
'''SETS METHODS'''
sunny.add(1234321)#add is used as like as append method in the list**
print(sunny)
sunny.update({1,2,3,4,5,6})
print(sunny)#updates the giveen set
set=set()
for i in range(0,4,2):
    set.add(i)
print(set)
a={1,2,3,4,5,6,7,8}
a.remove(2)#remove() methoc
print(a)
a.pop()#pop(),method
print(a)
b={12,13,2,3,4,5,}
b.pop()
print(b)
rithwik={1,2,3,4,5}
sathwik=rithwik.copy()
sathwik.add(234)
print(sathwik)

'''SET OPERATIONS'''
#1>UNION()
set1={1,22,3,4,5,6}
set2={98,97,96,95,94}
print((set1.union(set2)))
#2>intersection
a={1,2,3,10}
b={1,2,3,4,6,7}
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.isdisjoint(b))
print(b.issuperset(a))