#DICTIONARY IN PYTHON
#a dictionary in python is a list of key value of data seperated by the ,, between them and enclosed with the '''{}'''
#they are mutable(changable) we can add or remove any other values once dictionary is created but string is  imutable
#dupliactes are no allowed in the dictionary for example..>{1,21,1,2,3,45} here we will get error because 1 repeated two  times 
#dictionaries are used to store the values in the  key-value pairs
#dictionaries are case sensitive
#SYNTAX
'''
variable={key:value,1:'apple'}
'''
sathwik={1:'apple',2:'banana'}
print(sathwik)
'''DICTIONARY METHODS
1.clear() removes all the elements from the given dictionary
2.copy()  returns a copy of the dictionary
3.get()   returns the value of the specified key
4.items() returns a list containing a tuple for each key value pair
5.keys()  returns a list containing the dictionary keys
6.pop()   removes the elements with the specified key
7.update() updates the  dictionary with the  specified key values pairs
8.values() returns the list of all the values in the dictionary
'''
#in dictionary the values are not accessed by their index we have to access  their key values
print(sathwik[1])#output comes as apple (here the key acts as index)
a={1:"sathwik",2:"ritwik",3:"ayman"}
a[3]="ganesh"
print(a)#here the ayman is replaced by the ganesh


#1=clear()
a={1:"sathwik",2:"ritwik",3:"ayman"}
print(a.clear())
#2=copy()
a={1:"sathwik",2:"ritwik",3:"ayman"}
b=a.copy()
print(b)
#3=get()
a={1:"sathwik",2:"ritwik",3:"ayman"}
print(a.get(1))#output comes sathwik
#here the  get() is used to get the particular value with is stored in the particular key
#4=keys() and values() and items()
a={1:"sathwik",2:"ritwik",3:"ayman"}
print(a.keys())#here the output shows as the only keys
print(a.values())#here the output shows as the only values
print(a.items())#here the output shows as the total items in terms of the tuple
#5=updates()
a={1:"sathwik",2:"ritwik",3:"ayman"}
a.update({4:"ganesh"}) # here the dictionary adds the new element
a.update({2:"ganesh"}) # here the element 2:ritwik is replaced by the 2:ganesh as we changed the key
print(a)
#we cant change the key as like as value
#6=pop()
a={1:"sathwik",2:"ritwik",3:"ayman"}
a.pop(1)#here the pop function is used for removing the element to the particular key
print(a)
print(list(a))#converts from dictionary to list as ['sathwik','ritwik','ayman']
'''****************************************************************************'''
'''FOR LOOP IN DICTIONARY'''
b={1:"sathwik",2:"ritwik",3:"ayman"}
for i,j in b.items():
    print(i,j)
c={1:"sathwik",2:"ritwik",3:"ayman"}
for keys in c:
    print(keys,c.get(keys))  #check the output

#nested dictionary
a={
    1:"a",
    2:"b",
    3:{1:"aa"},
}
print(a[3][1])

#TUPLE IN PYTHON
#1.tuples are used to store multiple items in a single variable
#2.tuples are written with the round brackets ().
#3.tuples are IM MUTABLE (UNCHANGABLE)
#4.tuples allows duplicates
#SYNTAX OF THE TUPLE
#T=(20,"jessy",35.5,[30,60,90])
#in real time tuples are used in latitudes and longitutes 
#tuples are faster then the lists
#tuples make the code safe from any accidental modification
#tuples are used to store coordinates of other  locations
#no methods in the tuple so it is faster then the list
'''in tuple we should use buit-in functions'''
a=(1,2,3,4,5)
print(max(a))
print(min(a))
print(len(a))
print(sum(a))
print(list(a))#converts to list
print(a[4])#here output gives 5 in tuple index will work as like as in list
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)#concatinate 
#zip() 
s=zip(t1,t2)
print(tuple(s))
new=[]
for i,j in zip(t1,t2):#is used to add from one tuple to another tuple
    new.append(i+j)
print(tuple(new))#process to convert to tuple format...............
#>>>>>.
d=(1,2,3)
print(d*10)#repeats 1,2,3 upto 10 times
#MEMBERSHIP() BOOLEAN
f=(2,3,4,5,6,7,8,9,88,9)
print(2 in d)#gives true 
print(22 not in d)#gives true
#membership operator checks whether the elements present and gives the output in bool funtions like true or false
#IDENTITY OPERATOR()
t1=(1,2,3)
t2=(4,5,6)
print(t1 is t2)#false 
print(t1 is not t2)#true
'''tuple in for loop'''
n=[]
e=(1,2,3,4,5,6,7,8)
for i in e:
    n.append(i)
print(tuple(n))