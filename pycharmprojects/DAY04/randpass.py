from random import choice
from string import ascii_letters, digits
all_chars = ascii_letters +  digits
def randpass(x=8):

        result = '' #不对结果产生影响
        for i in range(x):
            result = [choice(all_chars) for  i in range(x) ]
            result = ''.join(result)
        return result

if __name__ == '__main__':
    print(randpass())
    #print(all_chars)