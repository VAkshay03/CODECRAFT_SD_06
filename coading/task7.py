#control statements/operators/loops/jumping operations..
#x+y here "+" is ooperator and (x,y are operends.)
#arthimatic operators/relational /assignment/logical/bitwise/membersship/
#conditional staments are also called as decision making statements,itteration statements are also called as looping staatements..
#syntax of if else>>
#if condition:
    #statement
#elif condition:
    #statement
#else:
    #statement
#if if condition is true and also elif condition is true then it executes only if statement....^^^^^^^^^
#when there is false in if condition only it executes next elif condition...)))
#if condition:statement one line..... is called ((short and if))
#true statemnt if condition else statement (no colon)
#example = a=1,b=2 print("this is true") if a<b else print("this is false") output checks LHS first..
#for value in range(strt,stop,skip):
                #print("value")
#(break is stop) and (continue is skip) and ((pass iss used for ignoring by compiler only taht particular statement)))
#end is used for it will not go to next line it will print in same line horizontal>>>
# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j,end=(" "))
#     print() # code for printing tables...
#differences in while and for loops
#in while loop we cant use range,and it is used for bulkk statements actually more people use for loop
#for value in conndition:
    #print(statement)
# len = int(input())
# l1=[]
# for i in range(len):
#     x=int(input())
#     l1.append(x)
# index=int(input())
# ele=int(input())
a=input("Sender : ")
key=int(input())
b=[]
l=len(a)
for i in a:
    if(i==" "):
        b.append(" ")
    else:
        c=ord(i)
        c=c-key
        if(c>122):
            c=c-26
        elif(c<97):
            c=c+26
        d=chr(c)
        b.append(d)
print("The encoded message : ")
for i in range(l):
    print(b[i],end="")
print("\n")

e=[]
for i in b:
    if(i==" "):
        e.append(" ")
    else:
        c=ord(i)               #"ord" gives ascii value of a character
        c=c+key
        if(c>122):
            c=c-26
        elif(c<97):
            c=c+26
        d=chr(c)              #"chr" gives the character of an ascii value
        e.append(d)
print("The decoded message : ")
for i in range(l):
    print(e[i],end="")