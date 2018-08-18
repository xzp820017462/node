list('abcd')
list((10, 20, 30))#元组转变成列表
tuple('abcd') #字符串变成元组
str([10, 20, 30]) #全部转变为字符串

users = ['bob', 'alice', 'john']
for i in range(len(users)):
    print('#%s: %s' %(i,users[i])) #给里面的列表里的index排序出来

list(enumerate(users)) #应用时不必转换,把列表转换成元组
for item in enumerate(users):
    print('#%s: %s' % (item[0],item[1]))

for ind, user in enumerate(users):
    print('#%s: %s' % (ind, user))

#reversed() 可以把内容反转输出并且不修改原来内容
#sorted() 按字母先后顺序进行排序

#字符编码: ASCII, ISO8859-1/Latin1, GB2312/GBK/GB18030










