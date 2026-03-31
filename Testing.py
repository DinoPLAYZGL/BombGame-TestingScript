from random import randint, shuffle

code = []
Gackomino = ["A","B","C","D"]
fredejackwe = sorted(Gackomino)
odibusrex = []

#jenevib

def Working(x):
    if x == 0:
        y = randint(1,4)
        if y == 1:
            print("0 x 2+ 0 = ?")
        elif y == 2:
            x = randint(1,10)
            print("0 /",x,"= ?")
        elif y == 3:
            x = randint(1,6)
            print(x,"-",x,"= ?")
        elif y == 4:
            print("0 + 0 = ?")
    if x == 1:
        y = randint(1,5)
        if y == 1:
            print("0 x 2 + 1 = ?")
        elif y == 2:
            x = randint(1,10)
            print(x,"/",x," = ?")
        elif y == 3:
            x = randint(1,6)
            print(x,"-",x - 1,"= ?")
        elif y == 4:
            print("1 + 0 = ?")
        elif y == 5:
            x = randint(5,25)
            print("(1 -",x,")(1 +",x,") +",x," (1 - 1 +",x,") = ?")
    if x == 2:
        y = randint(1,4)
        if y == 1:
            print("0 x 3 + 2 = ?")
        elif y == 2:
            print("4/2 = ?")
        elif y == 3:
            print("1 x 2 + 0 = ?")
        elif y == 4:
            print("(1 - 8)(2 + 8) +8 (2 - 1 + 8) = ?")
    if x == 3:
        y = randint(1,8)
        if y == 1:
            print("1 x 3 + 0 = ?")
        elif y == 2:
            print("15/5 = ?")
        elif y == 3:
            print("4 - 1 = ?")
        elif y == 4:
            print("(1 + 1)² - (1)² = ?")
        elif y == 5:
            print("2(1) + 1 = ?")
        elif y == 6:
            print("3/1 = ?")
        elif y == 7:
            print("√(5)² - (4)² = ?")
        elif y == 8:
            print("√9 = ?")
    if x == 4:
        y = randint(1,6)
        if y == 1:
            print("√16 = ?")
        elif y == 2:
            print("1 x 4 + 0 = ?")
        elif y == 3:
            print("(2 - 19) (2 + 19) +19 (2 - 2 + 19) = ?")
        elif y == 4:
            print("(1 - 19) (4 + 19) +19 (4 - 1 + 19) = ?")
        elif y == 5:
            print("(2 - 1) (2 + 1) + 1 (2 - 2 + 1) = ?")
        elif y == 6:
            print("(0)² + 2(0)(2) + (2)² = ?")
    if x == 5:
        y = randint(1,6)
        if y == 1:
            print("√25 = ?")
        elif y == 2:
            print("1 x 4 + 1 = ?")
        elif y == 3:
            print("(2 + 1)² - (2)² = ?")
        elif y == 4:
            print("2(2) + 1 = ?")
        elif y == 5:
            print("9 - 4 = ?")
        elif y == 6:
            print("1 x 3 + 2 = ?")
    if x == 6:
        y = randint(1,6)
        if y == 1:
            print("√36 = ?")
        elif y == 2:
            print("3 x 2 + 0 = ?")
        elif y == 3:
            print("(1 - 7)(6 + 7) +7 (6 - 1 + 7 ) = ?")
        elif y == 4:
            print("24/4 = ?")
        elif y == 5:
            print("(6 - 5)(1 + 5) +5 (1 - 6 + 5) = ?")
        elif y == 6:
            print("0 x 7 + 6 = ?")
    if x == 7:
        y = randint(1,7)
        if y == 1:
            print("√(25)² - (24)² = ?")
        elif y == 2:
            print("1 x 4 + 3 = ?")
        elif y == 3:
            print("21/3 = ?")
        elif y == 4:
            print("(3 + 1)² - (3)² = ?")
        elif y == 5:
            print("2(3) - 1 = ?")
        elif y == 6:
            print("0 x 8 + 7 = ?")
        elif y == 7:
            print("16 - 9 = ?")
    if x == 8:
        y = randint(1,9)
        if y == 1:
            print("√64 = ?")
        elif y == 2:
            print("16/2= ?")
        elif y == 3:
            print("1 x 7 + 1 = ?")
        elif y == 4:
            print("1 x 6 + 2 = ?")
        elif y == 5:
            print("2 x 4 + 0 = ?")
        elif y == 6:
            print("(8)(1) = ?")
        elif y == 7:
            print("4 x 2 + 0 = ?")
        elif y == 8:
            print("(4 - 13)(2 + 13) +13 (2 - 4 + 13) = ?")
        elif y == 9:
            print("0 x 9 + 8 = ?")
    if x == 9:
        y = randint(1,8)
        if y == 1:
            print("2(4) + 1 = ?")
        elif y == 2:
            print("1 x 6 + 3 = ?")
        elif y == 3:
            print("√81 = ?")
        elif y == 4:
            print("(9 - 14)(1 + 14) +14 (1 - 9 + 14) = ?")
        elif y == 5:
            print("(4 + 1)² - (4)² = ?")
        elif y == 6:
            print("2(4) + 1 = ?")
        elif y == 7:
            print("√(41)² - (40)² = ?")
        elif y == 8:
            print("(2)² +2(2)(1) +(1)² = ?")
        
while 1:
    for i in range(4):
        x = randint(0,9)
        code.append(x)
    shuffle(fredejackwe)
    print(fredejackwe)
    for i in range(4):
        odibusrex.append((fredejackwe[i], code[i]))
    print("\n------------------------\n-FOLLOW-THE-BIDMAS-RULE-\n------------------------")
    for x in range(4):
        Letter = Gackomino[x]
        if Letter == "A":
            for i in range(4):
                Counter = fredejackwe[i]
                if Letter == Counter:
                    print(Counter,"-",end=" ")
                    Working(odibusrex[i][1])
        elif Letter == "B":
            for i in range(4):
                Counter = fredejackwe[i]
                if Letter == Counter:
                    print(Counter,"-",end=" ")
                    Working(odibusrex[i][1])
        elif Letter == "C":
            for i in range(4):
                Counter = fredejackwe[i]
                if Letter == Counter:
                    print(Counter,"-",end=" ")
                    Working(odibusrex[i][1])
        elif Letter == "D":
            for i in range(4):
                Counter = fredejackwe[i]
                if Letter == Counter:
                    print(Counter,"-",end=" ")
                    Working(odibusrex[i][1])
    while 1:
        crack = input("\n------------------------\nPin - ")
        goishia = []
        for i in crack:
            goishia.append(int(i))
        if code == goishia:
            print("Cracked!")
            code = []
            fredejackwe = sorted(Gackomino)
            odibusrex = []
            break
        else:
            print("NotCracked!")
