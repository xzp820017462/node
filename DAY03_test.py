import sys
#def shangpin(x,y):
    #num = sys.argv[1]
    #xinghao = sys.argv[2]
counter = 0
all_choices = ['电脑', '显示器', '笔记本', '机械键盘']
while counter< 3:
    index = input("""请输入以下数字:(0)电脑
    1(显示器)
    (2)笔记本
    (3)机械键盘
    (4)添加信息
    (5)退出
    """)
    if index == '' :
        print("你没有输入数字,请重新输入")
        counter +=1
        continue
    index = int(index)
    if index == 4 :
        #num = int(input("请输入产品的编码"))
        xinghao = input("请输入产品的类型")
        last_result = all_choices.append(xinghao)
        print(all_choices)
    elif index == 5 :
        print("退出")
        break
    elif index > 5 and index < 0:
        print("你输入数字的范围不正确,请重新输入")
        counter +=1
        continue
    else:
        choice = all_choices[index]
        print(choice)
    #return  last_result

#print(shangpin(sys.argv[1],sys.argv[2]))

