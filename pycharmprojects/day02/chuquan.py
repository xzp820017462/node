import random
result = random.randint(1, 3)
if result == 1:
    s="拳头"
elif result ==2:
    s="剪刀"
elif result ==3:
    s="布"
guess = input("出拳头1剪刀2布3")
if guess == s :
    print("平局")
elif guess == "拳头" and s == "剪刀":
    print("你赢")
elif guess == "拳头" and s == "布":
    print("你输")
elif guess == "剪刀" and s == "拳头":
    print("你输")
elif guess == "剪刀" and s == "布":
    print("你赢")
elif guess == "布" and s == "剪刀":
    print("你输")
elif guess == "布" and s == "拳头":
    print("你赢")
print(s)


#computer = random.choice(['拳头', '剪刀', '布'])
#player = input('请出拳')
all_choices = ['拳头', '剪刀', '布']
win_list = [['拳头', '剪刀'], ['剪刀', '布'], ['布', '拳头']]
computer = random.choice(all_choices)
player = input("请出拳")


















