alist = [1, 50, 60, 100]
alist[0] = 10
alist[1:3] = [30,40]
alist[3:3] = [50,60,70,80] #在要添加的索引后面.进行取出判定.然后再进行添加
alist.append(30)
alist.reverse()#从大到小排序
alist.pop()#弹出最后一个
alist.pop(1)#弹出后面倒数第二个
alist.extend('abc') #字符串是每一个拆分开
alist.extend(['abc', 'xyz']) #元组,
alist.index(50)#可以返回50所在地方的索引
alist.insert(3, 1000) #在索引为3的地方插一个数字"1000"

