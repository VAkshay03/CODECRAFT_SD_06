'''
OUTPUT==
Enter your name : sathwik
for list of items press 1 or 2 for exit:

Rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/liter
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
colgate Rs 85/each

if you want to buy press 1 or 2 for exit : 1
Enter your items:sugar
Enter quantity:2
can i bill the items yes or no:yes
0 sugar 2 60

'''
#super market bill
name=input("enter your name : ")
lists='''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/liter
paneer  Rs 110/kg
maggi   Rs 50/kg
boost   Rs 90/each
colgate Rs 85/each
'''
qlist=[]
pricelist=[]
totalprice=0
final_price=0
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("option =  "))
if option==1:
    print(lists)
    buy=int(input("if you want to buy press 1 or 2 for exit:"))
    if buy==2:
        exit
    if buy==1:
        inp1=input("enter your item:")
        for item in items.keys():
            if inp1==item:
                print(inp1,items[inp1])
                quantity=int(input("quantity =  "))
                qlist.append(quantity)
                price=quantity*(items[inp1])
                pricelist.append(price)
                for i in items.keys():
                    if i==inp1:
                        S_NO=int(input("S.NO = "))
                        a=str(qlist)
                        b=str(pricelist)
                        print(S_NO,i,a[1:-1],b[1:-1])
                            