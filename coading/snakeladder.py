''''SNAKE AND LADDER GAME'''
rows = 10
columns = 10
num = 100
for i in range(rows):
    for j in range(columns):
        print('{:3}'.format(num), end=' ')
        num -= 1
    print()
snake_ladder=[12,24,30,35,40,88,93,96,100,8,13,25,31,54,65]
dice=[1,2,3,4,5,6]
position=0
player1=[]
player2=[]
option=int(input("option = "))
while True:
    if option==1:
        roll_dice=int(input("after dice rolled = "))
        if roll_dice in dice:
            position+=roll_dice
            if position in snake_ladder:
                if position==8:
                    print("climbed the ladder")
                    position=29
                if position==13:
                    print("climbed the ladder")
                    position=41
                if position==25:
                    print("climbed the ladder")
                    position=33
                if position==31:
                    print("climbed the ladder")
                    position=49
                if position==54:
                    print("climbed the ladder")
                    position=92
                if position==65:
                    print("climbed the ladder")
                    position=99
                if position==12:
                    print("snake eaten you")
                    position=3
                elif position==24:
                    print("snake eaten you")
                    position=15
                elif position==30:
                    print("snake eaten you")
                    position=17
                elif position==40:
                    print("snake eaten you")                
                    position=38
                elif position==88:
                    print("snake eaten you")
                    position=7
                elif position==93:
                    print("snake eaten you")
                    position=86
                elif position==96:
                    print("snake eaten you")
                    position=89
                elif position==100:
                    print("WON THE GAME")
                    break
            player1.append(position)
    print(*player1)
    if option==2:
        roll_dice=int(input("after dice rolled = "))
        if roll_dice in dice:
            position+=roll_dice
            if position in snake_ladder:
                if position==8:
                    print("climbed the ladder")
                    position=29
                if position==13:
                    print("climbed the ladder")
                    position=41
                if position==25:
                    print("climbed the ladder")
                    position=33
                if position==31:
                    print("climbed the ladder")
                    position=49
                if position==54:
                    print("climbed the ladder")
                    position=92
                if position==65:
                    print("climbed the ladder")
                    position=99
                if position==12:
                    print("snake eaten you")
                    position=3
                elif position==24:
                    print("snake eaten you")
                    position=15
                elif position==30:
                    print("snake eaten you")
                    position=17
                elif position==40:
                    print("snake eaten you")                
                    position=38
                elif position==88:
                    print("snake eaten you")
                    position=7
                elif position==93:
                    print("snake eaten you")
                    position=86
                elif position==96:
                    print("snake eaten you")
                    position=89
                elif position==100:
                    print("player 2 WON THE GAME")
                    break
            player2.append(position)
    print(*player2)
    