#cp /etc/passwd /tmp/mima
#fobj = open('mima')
fobj = open('/tmp/mima') #不指定打开模式,以r(只读方式打开)方式打开
data = fobj.read() #read 默认读取全部内容
print(data) #打印内容
data = fobj.read() #因为文件指针已经移动到尾部,没有数据可读,所在data是空字符串\
print(data) #空值
fobj.close() #关闭再打开就可以重置指针

fobj = open('/tmp/mima')
fobj.read(4) #指定读4字节,建议一次读1024的倍数
fobj.readline() #适合文本文件,读一行
fobj.readlines() #适合文本文件,把所有行读到列表中.
fobj.close()

fobj = open("/tmp/mima")
for line in fobj:
    print(line, end="")
fobj.close()

fobj = open('/tmp/mima' 'w') #
fobj.write('hello world \n') #写数据是,先放到缓冲区.当数据达到一定程度时,自动写入磁盘
fobj.flush() #立即将数据写入文件
fobj.writeline(['3rd line.\n', 'new line. \n' ]) # 写列表
fobj.close()#关闭文件时,数据自动写入磁盘

with open('/tmp/mima') as fobj:  #with语句结束,文件会自动关闭
    print(fobj.readline())

#seek(offset[, whence]) : 移动文件指针到不同的位置
#offset 是相对于某个位置的偏移量
#whence的值,0表示文件开头,1表示当前位置,2表示文件的结尾
#tell(): 返回当前文件指针的位置

fobj = open('/tmp/mima', 'rb') #rb以二进制来读取文件
fobj.tell() # 返回文件指针的位置
fobj.seek(10, 0) #第一个数字是便移量.第二个数字是相对位置,0是开头,1是当前,0是结尾,从当前位置向后移动10个字节
fobj.read(4) #从当前位置读4个字节,因为是bytes方式打开,所以显示b'XXXXXX'
fobj.seek(0,0)  #把指针重新指向开头
fobj.seek(-5, 2) #移动到文章末尾显示倒数第5个字节的位置,以'rb'才能写负数, 'r'不行

import sys
a = sys.stdin.readline()#读取键盘输入,回车也会作为字符\n读入
sys.stdout.write(a)  #输出正确数据
sys.stderr.write(a) #输出错误数据











