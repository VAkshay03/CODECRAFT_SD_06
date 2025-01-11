#problems on conditional stattements...
# print("hotel menu\n")
# print("1.breakfast\n2.lunch\n3.dinner\n")
# x=int(input("choice = "))
# if x==1:
#     print("breakfast")
#     print("1.idly\n2.dosa\n3.puri\n")
#     a=int(input("select = "))
#     if a==1:
#         print("idly=30rs")
#     elif a==2:
#         print("dosa=40rs")
#     else:
#         print("puri = 50rs")
# elif x==2:
#     print("lunch")
#     print("1.roti\n2.biryani\n3.fired_rice\n")
#     b=int(input("select = "))
#     if b==1:
#         print("roti=100rs")
#     elif b==2:
#         print("biryani=200rs")
#     else:
#         print("fired_rice=60rs")
# else:
#     print("lunch")
#     print("1.sweets\n2.icecream\n3.rice\n")
#     c=int(input("select = "))
#     if c==1:
#         print("sweets=200rs")
#     elif c==2:
#         print("icecreams=300rs")
#     else:
#         print("rice=160rs")
# print("dont forget to give the tip")
# i = 1
# while i <= 4:
#     j = 1
#     while j <= i:
#         print(2*j-1, end=" ")        important pattern......
#         j += 1
#     print()
#     i += 1
# i = 1
# while i <= 4:
#     j = 1
#     while j <= 7:
#         print(j, end=" ")
#         j += 2
#     print()
#     i += 1
# n=int(input("n ="))
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# i=1
# while i<=n:
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     i=i+1=0
# n=int(input("n =  "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
n=int(input("n = " ))
for i in range(2,n):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
            break
    if c==0:
        print(i)