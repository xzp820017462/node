'%12s  %8s' % ('name', 'age')#12和8代表的是宽度(右对齐)
'%-12s  %8s' % ('name', 'age') #-12和-8代表的也是宽度(右对齐)

###############################################以下内容不常用####################################################################
'%c' % 98 #ascii为98的字符转换出来
'%#o' % 30 #八进制数的形式
'%#x' % 30 #十六进制数的形式
'%e' % 100000 #科学记数法 1.0乘以10的5次方
'%f' % (5/3) #float浮点数形式
'%.2f' % (5/3) #小数点留两位
'%5.2f' % (5/3) #总共5的字符长度.小数占2位
'%+d' % -10  #正数钱+"+"号
'%010d' % 55 #总宽度为10,不足用0来补足

'{} is {} years old' .format('bob', 25) #bob is 25 years old
'{1} is {0} years old ' .format('25', bob) #
'{:<20}' .format('hello') #<左对齐塞满20个字符长度,">" 这个是右对齐,塞满20个字符