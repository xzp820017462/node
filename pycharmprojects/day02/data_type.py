names = '''
xuxuxu
xixixi
piuhad
'''
print(names)

py_str = 'python'
print(len(py_str))

print(py_str[len(py_str) -1 ])
py_str[2:4] #切片,2对应的t包含,4对应的o不包含所以结果是th
py_str[2:] #不写结尾表示到结尾
py_str[2:60] #切片没有下标,不会报错
py_str[0:2] #取出py
py_str[:2] #开头不写表示从头开始
py_str[:] #取出所有
py_str[::2] #2表示步长值
py_str[1::2] #从1开始步长值为2
py_str[::-1] #步长值为负数,表示从右向左取值

'*' * 50 #输出50"*"
'ab' * 20 # 输出20个ab

py_str.upper() #把内容变成大写
alist = ['bob', 'alice', 10, 20, [1, 2, 3]] #数组里啥都能放
3 in alist #false
alist[-1][1] #这个是把最后一个数组中的第二个索引取出来
['tom'] + alist #只有列表和列表才可以拼接,列表中只有一个项目
alist * 2 #得到一个更大的列表
alist.append(100) #向列表里添加内容

atuple = ('bob', 'alice', 10, 20) #远组可以判定为静态的列表
(100,)+atuple #这个必须要加逗号.如果不加逗号的话.小括号会自动剥离

##########################################--------字典---------#############################################################################
adict = { 'name': 'zhangsan', 'age': 25} #key-value形式
25  in adict # False 25是adcit字典的key吗?
'age' in adict # True 'age' 是字典的key
adict['name'] #返回zhangsan
#字典是无序的,
#容器里面什么都能放
#alist是找可变内存,而数字和字符串找的是固定内存


if 3 > 0:
    print('ok')
    print('yes')
if 'a' in 'abc' and 10 > 5:
    print('对')

if 10>20:
    print('yes')
else:
    print('no')

# 可以把数据类型直接当成判断条件
# 任何值为0的数字都是False,否则为True,
# 任何非空对象都是True,否则为False
if -0.0:
    print('yes') #不打印,因为这个数是0,不官符号如何都是0,非0的数都是0
if -0.1:
    print('yes') #打印,因为这个数不是0
if '     ' :
    print('yes') #打印,因为中间强调有"空格",空格是字符,所以打印
if '':
    orint('yes') #不打印,因为对象是null,所以为False

