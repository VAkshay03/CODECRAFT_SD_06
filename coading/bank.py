'''BASIC MINI BANK BILL PROJECT'''
name="sathwik"
passwords="sathwik@1234"
user_name=(input("enter username = "))
password=(input("enter your password = "))
s='''
1.credict
2.debit
3.mini statement
4.exit
'''
def credict():
    credit_amount=float(input("enter credit amount = "))
    print("amount after credit = ",Amount+credit_amount)
Amount=int(input("enter the Amount = "))
if name==user_name and passwords==password:
    while True:
        print(s)
        option=int(input("enter your option = "))
        if option==1:
            credict()
        elif option==2:
            debit_amount=float(input("enter debit amount = "))
            print("amount after debit = ",Amount-debit_amount)
        elif option==3:
            print("amount = ",Amount)
else:
    print("invalid details")