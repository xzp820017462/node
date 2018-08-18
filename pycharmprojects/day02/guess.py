import random

#result = random.randint(1, 10) #生成1~10之间的一个数字,包括1~10
#answer = input("guess the number:") #input进来的数字是字符串.不是数字
#answer=int(answer) #简单加工以下,把answer的字符串转变成数字.并重新复制给answer
#if answer  > result:
#    print('猜大了')
#elif answer < result:
#    print('猜小了')
#elif answer == result:
#    print('猜对了!!')
#
#print(result)





result2 = random.randint(1, 100)
running = True
while running :
    answer2 = input('guess the number: ')
    answer2=int(answer2)
    if answer2 > result2 :
        print('猜大了')
    elif answer2 < result2:
        print('猜小了')
    elif answer2 == result2:
        print('bingo!')
        running = False



print(result2)



















