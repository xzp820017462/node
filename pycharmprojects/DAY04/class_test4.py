from keyword import iskeyword
from string import ascii_letters, digits

first_char = ascii_letters + '_'
other_char = first_char + digits

def check_id(idt):

    if iskeyword(idt):
        return '你这个%s 是关键字' % idt

    if idt[0] not in first_char :
        return '1st invalid'

    for ind, ch in enumerate(idt[1:]):
        if ch not in other_char:
            return '你这个%s 是违规字符' % (ind+2)

    return '你这个%s 没毛病' % ind
