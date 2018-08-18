#num1 = 0
#num2 = 1
#for i in range(1, 10):
#    num3 = num1+num2
#    num1 = num2
#   num2 = num3
#  print(num3)

def gen_fib(l):
    fib = [0, 1]
    for i in range(l - len(fib)):
        fib.append(fib[-1] + fib[-2])
    return fib #函数如果没有return,默认返回None
   # c = fib
print(gen_fib(10))
l = int(input('length: '))
alist = gen_fib(l)
mylist = [10 + i for i in alist]
print(mylist)