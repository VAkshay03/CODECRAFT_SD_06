s="neil gogte z"
l=[]
m="abcdefghijklmnopqrstuvwxyz"
for i in range(0,len(s)):
    if s[i] in m:
        a=ord(s[i])+2
        if a > ord('z'):
            a=a-26
        b=chr(a)
        l.append(b)
    elif s[i]==" ":
        l.append(" ")
f="".join(l)
print(f)

# s=input()
# c=0
# l=[]
# for i in range(0,len(s)):
#     for j in range(0,len(s)):
#         b=s[i:j+1]
#         c=c+1
#         l.append(b)
# b=l.count("")
# print(c-b)
# s="[[]}"
# a=s[:len(s)//2]
# b=s[len(s)//2:]
# c=a+b
# m=s[0]
# n=s[-1]
# if c.startswith(m) and c.endswith(n):
#     print(a+"python"+b)
#     if s==n:
#         print("string is valid")
#     else:
#         print("string is not valid")
# else:
#     print("string is wrong")
# s=input("Enter text to encrypt: ")
# l=[]
# shift=int(input("Enter the shift value (a positive integer): "))
# if shift<0:
#     print("Shift value must be a positive integer.")
# if shift>0:
#     print("Shift value must be a positive integer.")
# else:
#     shift=int(input("Enter the shift value (a positive integer): "))
#     m="abcdefghijklmnopqrstuvwxyz"
#     for i in range(0,len(s)):
#         if s[i] in m:
#             a=ord(s[i])+shift
#             if a > ord('z'):
#                 a=a-26
#             b=chr(a)
#             l.append(b)
#         elif s[i]==" ":
#             l.append(" ")
#     f="".join(l)
#     print("Encrypted text: ",f)
s=input("Enter a string: ")
b=s.split()
print(min(b))
min=len(b[0])
for n in b:
    if len(n)<min:
        min=len(n)
for m in b:
    if min==len(m):
        print("Smallest word: ",m)
max=len(b[0])
for i in b:
    if len(i)>max:
        max=len(i)
for k in b:
    if max==len(k):
        print("Largest word: ",k)


