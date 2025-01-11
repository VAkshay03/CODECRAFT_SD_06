# num=int(input())
# l=[]
# for i in range(num):
#     n1,n2,n3=map(int,input().split())
#     avg=(n1+n2)/2
#     if float(avg)>n3:
#         l.append("YES")
#     else:
#         l.append("NO")
# for i in l:
#     print(i)
'''########################################################################################'''
# num=int(input())
# l=[]
# for i in range(1,num+1):
#     a,b=map(int,input().split())
#     if a<=6:
#         l.append(b*i)
#     elif a>=6 and a%6==0:
#         d=a//6
#         l.append(b*d)
#     elif a>=6 or a%6==0:
#         d=a//6
#         l.append(b*(d+1))
# for j in l:
#     print(j)
"""##############################################################################"""
# n=int(input())
# l=[]
# for i in range(n):
#     a=int(input())
#     sub_time=10
#     b=a+3
#     if b<=sub_time:
#         l.append("YES")
#     else:
#         l.append("NO")
# for j in l:
#     print(j)
'''############################################################################'''
# n=int(input())
# l=[]
# for i in range(n):
#     n1,n2,n3=map(int,input().split())
#     b=n1*n2
#     per=(n3/b)*100
#     if per>50:
#         l.append("YES")
#     else:
#         l.append("NO")
# for j in l:
#     print(j)
'''###############################################################################'''
# n=int(input())
# a=list(map(int,input().split()))
# b=a[:n]
# c=0
# s=0
# for i in b:
#     if i%2==0:
#         c=c+1
#     else:
#         s=s+1
# if c>s:
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY FOR BATTLE")
'''#################################################################################'''
# n=int(input())
# l=[]
# for i in range(0,n):
#     cred,bills=map(int,input().split())
#     b=cred*bills
#     if b>=100:
#         b//=100
#         l.append(b)
#     else:
#         b=0
#         l.append(b)
# for j in l:
#     print(j)
'''##########################################################################'''
# n = int(input())
# l1 = []
# for i in range(n):
#     a, b, c = map(int, input().split())
#     l=[]
#     l.append(a)
#     l.append(b)
#     l.append(c)
#     count_ones = l.count(1)
#     count_others = len(l) - count_ones
    
#     if count_others > count_ones:
#         l1.append("water filling time")
#     else:
#         l1.append("not now")

# for result in l1:
#     print(result)
'''################################################################################'''
# n=int(input())
# l=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     c=a*b
#     if c%4==0:
#         d=c//4
#         l.append(d)
#     else:
#         d=c//4
#         f=d+1
#         l.append(f)
# for j in l:
#     print(j)
'''#############################################################################'''
# n=int(input())
# l1=[]
# for i in range(n):
#     a,b,c,d=map(int,input().split())
#     l=[a,b,c,d]
#     f=l.count(1)
#     if f>0:
#         l1.append("OUT")
#     else:
#         l1.append("IN")
# for j in l1:
#     print(j)
'''#################################################################################'''
n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        l.append("CAR")
    elif a<b:
        l.append("BIKE")
    else:
        l.append("SAME")
for j in l:
    print(j)
    
        
    