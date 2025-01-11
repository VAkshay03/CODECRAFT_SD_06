#1>check whether the number is even or odd
# num=int(input("number = "))
# if num%2==0:
#     print("EVEN")
# else:
#     print("ODD")
#2>check whether the number is positive or negative
# num=int(input("number =  "))
# if num>0:
#     print("POSITIVE")
# elif num==0:
#     print("neither +ve nor -ve")
# else:
#     print("NEGATIVE")
#3>to print all odd numbers in given range
# num=int(input("number =  "))
# print("odd numbers upto the given range")
# for i in range(1,num):
#     if i%2!=0:
#         print(i,end=" ")
#4>write a program check whether it is palindrome or not
# num=int(input("number =  "))
# sum=0
# temp=num
# while num>0:
#     r=num%10
#     num=num//10
#     sum=(sum*10)+r
# if sum==temp:
#     print("palindrome")
# else:
#     print("not a palindrome")
#5>reverse of a number
# num=int(input("number =  "))
# while num>0:
#     r=num%10
#     num=num//10
#     print(r,end="")
#6>python program that the numbers are not divisble by 2 and 3
# num=int(input("number =  "))
# for i in range(1,num):
#     if i%2!=0 and i%3!=0:
#         print(i)
#7>python program to print all numbers which are divisible by the number taken by  the user
# lower=int(input("lower =  "))
# upper=int(input("upper =  "))
# num=int(input("number =  "))
# for i in range(lower,upper+1):
#     if i%num==0:
#       print(i,end=" ")
#8>programe to print sum of digits in a givenn number
# num=int(input("number =  "))
# sum=0
# while num>0:
#     rem=num%10
#     num=num//10
#     sum=sum+rem
# print(sum)
#9>programe to print count the digits in a give digit
# num=int(input("number =  "))
# count=0
# while num>0:
#     rem=num%10
#     num=num//10
#     count=count+1
# print(count)
#10>find all the divisors of a given number
# lower=int(input("lower =  "))
# upper=int(input("upper =  "))
# num=int(input("number =  "))
# a=[]
# for i in range(lower,upper+1):
#     if num%i==0:
#       a.append(i)
# a.sort()
# print("smallest divisor")
# print(a[1])
'''printing table'''
# num=int(input("enter number = "))
# for i in range(11):
#     print(num," X ",i," = ",num*i)
'''
1. User must enter 5 different values and store it in separate variables.
2. Then sum up all the five marks and divide by 5 to find the average of the marks.
3. If the average is greater than 90, “Grade: A” is printed.
4. If the average is in between 80 and 90, “Grade: B” is printed.
5. If the average is in between 70 and 80, “Grade: C” is printed.
6. If the average is in between 60 and 70, “Grade: D” is printed.
7. If the average is anything below 60, “Grade: F” is printed.

'''
# math=int(input("marks in math:"))
# phy=int(input("marks in phy:"))
# chem=int(input("marks in chem:"))
# tel=int(input("marks in telugu:"))
# hin=int(input("marks in hindi:"))
# avg=(math+phy+chem+tel+hin)/5
# print(avg)
# if(avg>90):
#     print("grade A")
# elif(avg>=80 and avg<=90):
#     print("grade B")
# elif(avg>=70 and avg<=80):
#     print("grade C")
# elif(avg>=60 and avg<=70):
#     print("grade D")
# else:
#     print("FAIL")
'''prime numbers in the given range'''
# num=int(input("enter number:"))
# for i in range(2,num):
#     flag=0
#     for j in range(1,num):
#         if i%j==0:
#             flag=flag+1
#     if flag==2:
#         print(i)

'''PERFECT NUMBER'''
# num=int(input("enter the number:"))
# sum=0
# for i in range(1,num):
#     if (num%i==0):
#         sum=sum+i
# if (sum==num):
#     print("perfect number ")

# '''ARMSTRONG NUMBER'''
# n=int(input("enter any number:"))
# c=0
# sum=0
# a=n
# while a>0:
#     a//=10
#     c=c+1
# a=n
# while a>0:
#     r=a%10
#     sum=sum+r**c
#     a//=10
# if n==sum:
#     print("armstrong number")

'''to print sum of first n natural numbers'''
# def value(n):
#     sum=0
#     for i in range(n+1):
#         sum=sum+i
#     print(sum)
# n=int(input())
# value(n)

'''prime factors of a nnumber'''
# n=int(input("eenter a number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

'''amicable number'''
# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))
# sum=0
# for i in range(1,n1):
#     if n1%i==0:
#         sum=sum+i
# s=0
# for j in range(1,n2):
#     if n2%j==0:
#         s=s+j
# if sum==n2 and s==n1:
#     print("both are amicable number")


'''no of possibilities'''
# n1 = int(input("n1:"))
# n2 = int(input("n2:"))
# n3 = int(input("n3:"))
# my_list = []
# my_list.append(n1)
# my_list.append(n2)
# my_list.append(n3)
# new=[]
# for i in my_list:
#     if i==n1:
#         for j in my_list:
#             if j==n2:
#                 temp=i
#                 i=j
#                 j=temp
#                 c=n3
#                 new.append(i)
#                 new.append(j)
#                 new.append(c)
#                 break
#         print(new)
# new.reverse()
# print(new)
# print(my_list)
# my_list.reverse()
# print(my_list)
# new1=[]
# for i in my_list:
#     if i==n2:
#         for j in my_list:
#             if j==n3:
#                 temp=i
#                 i=j
#                 j=temp
#                 d=n1
#                 new1.append(d)
#                 new1.append(i)
#                 new1.append(j)
#                 break
#         print(new1)
# new1.reverse()
# print(new1)

# '''fibonici series'''
# n=int(input("enter any number:"))
# a=0
# b=1
# c=a+b
# for i in range(1,n):
#     a=b
#     b=c
#     c=a+b
#     print(c)

''''''

