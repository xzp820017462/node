import random
number = random.randint(1, 10)
while True :
    player = input("input the number")
    player = int(player)
    if number == player:
        print("猜对了")
        break
    elif number < player:
        print("猜大了")
    else:
        number > player
        print('猜小了')