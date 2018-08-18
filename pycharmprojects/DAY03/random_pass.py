import random
import sys
def ran_pass(w):
    AllBytes = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#a = len(AllBytes)
#print(a)
    b = ''
    for i in range(w):
        c = random.choice(AllBytes)
        #print(c, end='')
        b += c
    return b
#input("do you like ♂van youxi ?")
print(ran_pass(w=int(sys.argv[1])))
#random_pass(sys.argv[1])


