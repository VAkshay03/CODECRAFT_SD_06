'''FUNCTIONS'''
#function is a block of a code which executes only when it is called...
#syntax of the function
'''
def my_sum(a,b):#here we  call the a,b as parameters in function definition
    return a+b
my_sum(10,20)'''#here we  call the a,b as arguments in function call

# def sathwik(a,b):#code block
#     sum=a+b
#     print("this is function",sum)
# sathwik(10,20)#function call

#if a function has one parameter then it is called single parameter function
#if a function has more then one parameter then it is called multiple parameter function

# def my_sum(a,b):
#     print(a+b)
# my_sum(10,20)
# my_sum(100,33)


# def akki(name):
#     print("hii",name)
# name=input("enter your name:")
# akki(name)

# def akki(**name):        #arbritraty parameter * stores in tuple format
#     print("hii",name)
# name=input("enter your name:") #keywords parameter ** stores in dictionary format
# akki(name="sathwik",age=25)



# def outer_function():
#     print("students ages list")
#     def inner_function():                 #nested function
#         print("this is inner funnction")
#     inner_function()
# outer_function()

'''module= collection of many functions'''

# from call import *
# d=sum(1,22)
# print(d)
# sub(2,1)
# mul(2,100)#here the function calls from the call.py python file


'''ADVANCE FUNCTIONS'''
#map function is used change th structure of the data in the output
#filter function not changes the sturcture of the data
#reduce function combines every data


'''LAMBDA FUNCTION'''
#a lamda function is a small unknow or anonymous function
#a lamda function can take any no of arguments but it takes only single expression
#   EXAMPLE     f=lamda a,b,c:a+b+c

# f=lambda a,b,c:a+b+c
# print(f(2,3,4))

# l1=[1,2,3,4,5]
# l2=[]
# for i in l1:            #lambda function using the for loops
#     t=lambda a:a+1
#     c=t(i)
#     l2.append(c)
# print(l2)


#lambda is a single line function
#filter function accepts true and executes 

'''FILTER FUNCTION'''

'''
filter(function,sequence)
parameters:
function: function that tests if each element of a 
sequence true or not
sequence : sequence which needs to be filtered , it ca be sets,lists,tuples, or containers of any iterators.
Returns:
returns are iterator that is already filtered.


'''


#exaample 

# ages=[1,2,3,10,20]

# def my_fun(x):
#     if x<18:
#         return True
#     else:
#         return False
    
# youngs=filter(my_fun,ages) #loops here or iterable
# print(list(youngs))

'''MAP FUNCTION'''
'''
the pytthon map() function is used to return a list of results 
after applying a given function to each item of a iterable(list,tuple etc.)

map(function,iterables)
'''

# def cal(n):
#     return n+n
# num=(1,2,3,4)
# f=map(cal,num)
# print(list(f))


'''
reduce() is used to get output in single value
'''

# from functools import reduce
# #reduce(function,sequence)
# d=reduce(lambda a,b: a+b,[1,2,3,4])
# print(d)




# def even(x):
#     if x%2==0:
#         print(x)
# nums=[11,22,33,44,55]
# filters=list(filter(lambda x:x%2==0,nums))
# print(filters)
# nums=[11,22,33,44,55]
# maps=list(map(lambda x:x**2,nums))
# print(maps)
    

# def num1(a,b,c):
#     if a>b and a>c:
#         print("a is max")          ### to check max of three numbers
#     elif b>a and b>c:
#         print("b is max")
#     else:
#         print("c is max")
# num1(12,6,20)
        

# def num(a):
#     for i in range(1,11):        #multiplication table
#         print(a," X ",i," = ",a*i)
# num(6)




# from functools import reduce
# a=reduce(lambda a,b:a*b,[1,3,4])   #by using the reduce()
# print(a)



l1=[1,2,3,4,5]
l2=[]
for i in l1:            #lambda function using the for loops
    t=lambda a:a
    l=i[0]
    c=t(l)
    l2.append(c)
print(l2)