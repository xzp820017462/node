import random
#while win_computercount <2 or win_playercount < 2 :
win_computercount = 0
win_playercount = 0
while win_computercount < 2 and win_playercount < 2 :
    all_choices = ['石头', '布', '剪刀']
    computer = random.choice(all_choices)
    win_list = [['石头', '剪刀'], ['布', '石头'], ['剪刀', '布']]
    index = input("""(0)石头
    (1)布
    (2)剪刀
    """)

#while win_computercount <2 or win_playercount < 2 :
    index = int(index)
    player = all_choices[index]
    if player == computer :
        print('平局')
        continue
    elif [player, computer] in win_list:
        print('you win!')
        win_playercount +=1
        continue
        if win_playercount == 2:
            break
    else:
        print('you lose!')
        win_computercount+=1
        continue
        if win_computercount ==2 :
            break

if win_playercount == 2:
    print('player win!')
else:
    print('computer win!')




