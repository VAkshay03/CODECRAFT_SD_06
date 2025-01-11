'''problems on lists from the greeks for greeks...'''
#1>interchanging last and the first terms of the given list
'''
newlist=[]
list=[1,2,3,4,5,6,7]
temp=list[0]
list[0]=list[6]
list[6]=temp
for i in list:
    newlist.append(i)
print(newlist)'''
#2>swapping any two elements the list
'''
list=[1,2,3,4,5]#always the index starts with the zero
pos1,pos2=2,4
list[pos1],list[pos2]=list[pos2],list[pos1]
print(list)'''
#3>to find the length of the list
'''
list=[1,2,3,4,5,6]
print(len(list))  #first method
c=0
for i in list:
    c=c+1          #second method
print(c)'''
#4>check whether the number is present in the given list
'''
list=[1,2,3,4,5,6]
s=3
if s in list:
    print("list exist")
else:
    print("list doesn't exist")
'''
#5>clear the list
'''
list=[1,22,3,4]
print("the list before clearing")
print(list)
newlist=(list.clear())
print("the list after clearing")
print(newlist)'''

#6>reverse the list
'''
list=[1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)'''

#7>count the occarance of the particular digit in the given list
'''
list=[1,2,3,4,5,2,2,2,3,4]
x=int(input("x="))
c=0
for i in list:
    if i==x:
        c=c+1
print(x,"occured",c,"times")'''

#8>to print the  sum and the  average of the list
'''
list=[1,2,3]
sum=0
c=0
for i in list:
    sum=sum+i
    c=c+1
print("sum of the digits of the given list = ",sum)
print("no of digits in the given list = ",c)
avg=sum/c
print("average of the given list = ",avg)'''

#9>to print the squares of the list
'''list=[]
print("enter the length of the list=",end=" ")
l=int(input())
for i in range(l):
    a=int(input())
    list.append(a)
newlist=[]
for j in list:
    newlist.append(j*j)
print("newlist after squarinng each number",end=" ")
print(newlist)'''

#10>copying the list
'''list=[]
print("enter the length of the list=",end=" ")
l=int(input())
for i in range(l):
    a=int(input())
    list.append(a)
newlist=list.copy()
print(newlist)'''

#11>sort the list
'''list=[]
l=int(input())
for i in range(l):
    a=input()
    list.append(a)
print("before sorting = ",end=" ")
print(list)
list.sort()
print("after sorting = ",end=" ")
print(list)'''

#12>adding the two list
'''list=[]
l=int(input())
for i in range(l*2):
    a=int(input())
    list.append(a)
newlist=[]
for j in range(0,l*2,2):
    k=list[j]+list[j+1]
    newlist.append(k)
print(newlist)'''

#13>replacing the particular elements in the given list
'''list=[]
l=int(input())
for i in range(l):
    a=int(input())
    list.append(a)
old=int(input())
new=int(input())
for j in range(l):
    if list[j]==old
        list[j]=new
print(list)'''

#14>python program to remove particular element chosen by the user
'''list=[]
l=int(input())
for i in range(l):
    a=int(input())
    list.append(a)
n=int(input())
list.remove(n)
print(list)'''

#15>python programee to insert the element the given list
'''list=[]
l=int(input())
for i in range(l):
    a=int(input())
    list.append(a)
n=int(input())
index=int(input())
list.insert(index,n)
print(list)'''

'''--------------------PROBLEMS BASED ON THE STRINGS-----------------------'''









