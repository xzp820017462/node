import random

all_choices = ['拳头', '剪刀', '布']
win_list = [['拳头', '剪刀'], ['剪刀', '布'], ['布', '拳头']]
prompt = """(0)拳头
(1)布
(2)剪刀
"""
computer = random.choice(all_choices)
ind = int(input(prompt))
player = all_choices[ind]
print('你出了: %s, 计算机出的是: %s' % (player, computer))
if player == computer :
    print("平局")
elif [player, computer]:
    print("你赢")
else:
    print("你输")
