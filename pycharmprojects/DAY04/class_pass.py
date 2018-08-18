new_list = []

def push_it(): #这个可以看出来,我们用这个push把内容推进去.里面内容就是推进去
    new_list.append(input("请输入你要输入的内容: "))

def pop_it(): #因为最后数据是先进后出,也就是说我们要把后来的数据先T掉.所以我们用pop
    if new_list :
        new_list.pop()
def view_it():#就是简简单单的查看内容
    print(new_list)
def show_menu():#这里左的是函数的调用
    cmds = {'0':push_it, '1':pop_it, '2':view_it}
    prompt = """(0)push
(1)pop
(2)view
(3)exit
请输入你的选项(0/1/2/3)
    """
    while True :
            choice = input(prompt)
            if choice == '' :
                print("你没有输入任何东西,请重新输入")
                continue
            else:
                choice = choice.strip()[0]

            if choice == '3' :
                break
            elif choice == '0' :
                push_it()
            elif choice == '1' :
                pop_it()
            elif choice == '2' :
        in        view_it()

if __name__ == '__main__':
    show_menu()









