#[3 + i for i in range(10)] #循环控制3+运行多少次
#[3 + i for i in range(10) if i % 2 == 1]#判断条件作为过滤条件

#wangduan =["192.168.1."]
ab=["192.168.1.%s" % i for i in range(1, 255)   ]
print(ab)