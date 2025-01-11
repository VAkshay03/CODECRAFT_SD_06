n=int(input())
l=[]
for i in range(0,n):
    name=input()
    marks=float(input())
    l.append([name,marks])
print(l)
new=[]
for i in l:
    for j in range(1,len(i)):
        a=i[j]
        new.append(a)
d=min(new)
print("min value is :",d)
new.remove(d)
secmin=min(new)
print("second min is :",secmin)
for k in l:
    for m in range(0,len(k)):
        if d==k[1] or secmin==k[1]:
            print(k[0])
            break
