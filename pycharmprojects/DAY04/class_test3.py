from string import ascii_letters, digits
from keyword import iskeyword

first_chs = ascii_letters + '_' #第一个字符要是下划线或者字母开头
other = first_chs + digits #其他字符都是


def check_mes(idt):
    if iskeyword(idt):    #函数中有多个return,只会返回一个return
        return '%s is keyword!' %idt
    if  idt[0] not in first_chs:
        return '1st invalid'
    for ind,ch in enumerate(idt):
        if ch not in other :
            return '第%s个符号错了' % ind+2

    return '你输入的%s是正确的' % idt

if __name__ == '__main__':
    idt = input("代检查的标示符")
    print(check_mes(idt))

