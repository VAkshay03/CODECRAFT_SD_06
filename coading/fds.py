'''STRINGS'''
''' prob 1 '''
# s="hello"
# print(len(s))#length of the string
'''prob 2'''
# s=input()
# c=1
# dic={}
# for i in s:
#     dic[i]=s.count(i)
# print(dic)
'''prob 3'''
# s=input()
# if len(s)>=2:
#     print(s[0]+s[1]+s[-2]+s[-1])
# else:
#     print("Empty string")
'''prob 4'''
s=input()
c=0
for k in range(0,len(s)):
    for m in range(k+1,len(s)):
        if s[k]==s[m]:
            c=1
            break
if c==1:
    z=s[k]
print(z)
for i in range(1,len(s)):
    if s[i]==s[k]:
        s=s.replace(s[i],"$")
l=[]
for j in s:
    l.append(j)
l[k]=z
print(l)
m="".join(l)
print(m)
'''prob 5'''
# s1=input()
# s2=input()
# a=s1[:2]
# b=s2[:2]
# s1=s1.replace(a,b)
# s2=s2.replace(b,a)
# print(s1+" "+s2)
'''prob 6'''
# s=input()
# if "ing" in s:
#     print(s+"ly")
# else:
#     print(s+"ing")


