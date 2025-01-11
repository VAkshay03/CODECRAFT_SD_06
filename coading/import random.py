import random
i=0
j=0
p1,p2,p3="rock","paper","scissors"
while True:
    d = int(input("enter option: "))
    if d==1:
        opt = (input("sathwik's chance = "))
        l = ["rock", "paper", "scissors"]
        computer = random.choice(l)
        print("computer = ", computer)
        if computer==opt:
            print("draw")
        elif (computer == "rock" and opt == "paper") or (computer == "scissors" and opt == "rock") or (computer == "paper" and opt == "scissors"):
            print("won")
            i=i+1
        elif (computer== "rock" and opt == "scissors") or (computer == "scissors" and opt == "paper") or (computer == "paper" and opt == "rock") :
            print("lost")
            j=j+1
    else:
        print("game ended")
        break
print("sathwik got",i,"points")
print("computer got",j,"points")
if i>j:
    print("sathwik won the game")
elif i<j:
    print("computer won the game")
else:
    print("draw")
