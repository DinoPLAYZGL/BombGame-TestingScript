from random import randint
num = []
while 1:
    g = input()
    for i in range(4):
        x = randint(0,9)
        num.append(x)
    print(num)
    num.clear()
