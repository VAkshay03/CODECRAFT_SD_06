#calcualting simple interest and compound interest
print("SIMPLE INTEREST")                                      #TASK 5....
principle_amount=float(input("principle_amount = "))
rateof_Interest=float(input("rateof_Interest = "))
time=int(input("time = "))
simple_interest=(principle_amount*rateof_Interest*time)/100
print("simple_interest = ",simple_interest)

#calculating compound interest
print("COMPOUND INTEREST")
P=int(input("P= "))
r=int(input("r = "))
n=int(input("n = "))
t=int(input("t = "))
CI=P*(1+r/n)**(n*t)
print("COMPOUND INETEREST = ",CI)