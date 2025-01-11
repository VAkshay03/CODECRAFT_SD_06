#a list is used to store the sequence of the data of various type.example=list=[12,1.23,'sathwik',[2,3,4]]
#(((mutable means changeable))) ((((immutable means not changes)))))
#LIST IN PYTHON=2|3|4|5|6|7|--->>element(value)
#               0 1 2 3 4 5 --->>index LHS to RHS..
#synntax is list_name(varaible)=elements and index starts with zero..
#n=no of elements then index=n-1..
#in python index are deivided inn two types 1}forward or positive(+ve)index 2}negative backward(-ve)index 
#negative index starts with -1  and ends with the n numbers depends on the elements... from RHS to LHS
#LIST=[start,stop,skip]
sathwik=[]
print(type(sathwik))#output=class<list>
sathwik=[1,2.23,'python',True]
#sathwik=list(1,2.23,'raju') used to converting from list to tuple
sathwik=list[1,2.23]#this is also very  true....
print(sathwik)
_1=[2.2,3.4,5.5,1,2,3,4,5]
print(_1[1:3]) #output=3.4,5.5>>>>.
print(_1[-8]) #output = 2.2>>>
#SLICING
sath_wik=[7,3,4,3,34,64,'True']
print(sath_wik)#prints list
print(sath_wik[0:6:3])#jumps forward 2 steps if 2 means jumps 1 step
print(sath_wik[6:0:-2])#jumps backward 1 step if -4 means jumps 3 steps
print(sath_wik[5:0])#output=[]nill 
#here if we want to go in backward direction the skip is must and important.....
print(sath_wik[:6])#the before data will print ....
print(sath_wik[6:])#the after data will print....
print(sath_wik[:-1])#output is from 7 to true
print(sath_wik[::-1])#the ouput comes in reverse order....
print(sath_wik[6:6])#the output comes empty []>>>>
################LISTS METHODS(350 METHODS)
'''append()
copy()
clear()
count()
extend()               10 LIST METHODS
index()
insert()
pop()
remove()
reverse()
sort()
'''

#LIST METHOD SYNTAX IS (((VARIABLE.LIST_METHOD))))
#1.append
a=[1,2,3,4,4525,23,63,6]
a.append([1,2,3])#the append is used to add the extra data in list the ouput is [1,2,3,4,4525,23,63,6,123] here 123 is added
print(a)
#2.extend
b=[1,2,3,3,3,3,3,3,3,4,4525,23,63,6]
b.extend([123])
print(b)
#here the  difference between the  append and extend method is
#the append will print as same as present in the ()paranthesis
#BUT the extend is print only if it contains the squarebackets inside the ()
#3.count
print(b.count(3))#count how many elements present in it...
#4.index
print(b.index(4525))#output index of 4525 is 10
#5.len
print(len(a))#checks the lengthn of  the index not elements....
#6.clear
#print(a.clear())#clear the total data...
x=[10,2,3,4,5]
y=x
print(y) #stores the same value
#the above example is shown by using
#7.copy
y=x.copy()
print(y)#output is [1,2,3,4,5]
#x.append(123)
#print(y) # the 123 is not included this is the use of copy method in the list...
#print(x.pop(3))
(x.remove(4))
print(x)
(x.sort())
print(x)# sorting is for to convert from (((AC TO DC OR DC TO AC))))
_5=[1,4,3,0]
_5.reverse()
print(_5)# reverse the list...
#TO GET FROM  ASCENDING to DESCENDING ORDER
_5.sort(reverse=True) #prints from descending order to ascending order.......
print(_5)
#LIST COMPREHENSION WITH CONDITIONAL STATEMENTS.....
#SYNTAX=[Expression for item in itterable]
list=[x**2 for x in [1,2,3,4]]
print(list)#prints the square of  the  every number..
o=["even" if i%2==0 else "odd" for i in range(1,10)]
print(o)
newlist=[]
for x in ["apple","banana","cherry","kiwi","mango"]:
    if "a" in x:
        newlist.append(x)
print(newlist)
a=[]
for x in [1,2,3,4,5,6,7,8]:
    if x%2==0:
        a.append(x)
print(a)
#in the above two codes the append() is used when the if statement is true so it will execute and the append is used here to add avlue in a[[list]]
s=[1,2,3,4,5]
for i in range(len(s)):
    if s[i]==3: #code for to find the particular index for an element in an list...
        print(i)
#replacemethod replace()
