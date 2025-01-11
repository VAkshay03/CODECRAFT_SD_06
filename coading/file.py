# import os
# n = os.getcwd()
# print(type(n),n)
# os.chdir("C:\\Users\\Bharath Elakurthi\\Desktop\\FDS\\python")
# print(os.getcwd())
# os.makedirs("FDS\\python",exit_ok=True)
# f= open("FDS\\python\\breakfast.txt","w")
# f.write("1.idli,2.dosa,3.samosa")
# with open("FDS\\python\\breakfast.txt","w") as fp:
#     fp.write("1.idli,2.dosa,3.samosa")

# path="C:\\Users\\Bharath Elakurthi\\Documents"
# with open("abc.txt","w") as fp:
#     fp.write("hello how are you?")
# print("written  in the file")

l=[1.2,1.21,1.23,1.24,1.25]
j=1.21
for i in l:
    if i==j:
        print(i)