l1=[9,9,9,9,9,9,9]
l2=[9,9,9]
a=len(l1)
b=len(l2)
sum1=0
for i in range(len(l1)-1,-1,-1):
    sum1=sum1+l1[i]*10**(i)
c=sum1
sum2=0
for j in range(len(l2)-1,-1,-1):
    sum2=sum2+l2[j]*10**(j)
d=sum2
e=c+d
f=str(e)
l=[]
for k in f:
    l.append(int(k))
l3=l[::-1]
print(l3)