import random
win_player = 0
win_computer = 0
all_choices = ["拳头", "剪刀", "布"]
win_list = [["拳头", "剪刀"], ["剪刀","布"], ["布", "拳头"]]
while win_computer < 2 and win_player < 2 :
    computer = random.choice(all_choices)
    index = input("""(0)拳头
    (1)剪刀
    (2)布
    """)
    index = int(index)
    player = all_choices[index]
    print('你出的是: %s , 电脑出的是: %s' % (player, computer))
    if player == computer :
        print("平局")

    elif [player, computer] in win_list:
        win_player += 1
        print("you win!")
        continue
        if win_player ==2:
            print('you win!')
            break
    else:
        print ("you lose!")
        win_computer += 1
        continue
        if win_computer == 2 :
            print('you lose!')
            break