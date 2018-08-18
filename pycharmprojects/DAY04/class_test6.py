new_list = []  # 全局边量,从定义开始到程序结束都可见可用


def push_it():
    item = input('item to push: ')
    new_list.append(item)


def pop_it():
    if new_list:
        print('pop:%s' % new_list.pop())


def view_it():
    print(new_list)


# cmds = {'0': push_it(), '1': pop_it(), '2':view_it()} #只把名字家进来.不要加括号()cmds是字典.字典里是函数.把函数名写入即可.写"()"就会直接调用函数了

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = '''(0) push it 
(1) pop it 
(2) view it 
(3) exit
please input your choice(0/1/2/3):
'''

    while True:
        choice = input(prompt).strip()[0]  # 把p取出来了
        if choice not in '0123':
            print("invaalid input. try again")
            continue

        if choice == '3':
            break

        cmds[choice]()

    # if choice == '0':
    #        push_it()
    # elif choice == '1':
    #       pop_it()
    # elif choice == '2':
    #      view_it()


if __name__ == '__main__':
    show_menu()
