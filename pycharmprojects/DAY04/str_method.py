win_path = 'c:\temp\newdir' #这个是两个意思.
win_path2 = r'c:\temp\newdir' #这个是原来意思

astr = '\thello'
astr.strip() #去除两端空白字符
astr.lstrip() #去除左边空白字符
astr.rstrip() #去除右边空白字符

hi = 'hello world'
hi.title()#所有字符串变成大写.但是本身因为是字符串不可变,所以不会变
'hao123'.islower()
'hao123'.isdigit()
'hao123'.isidentifier()#是不是可定义的.
hi.center(50) #居中,符号和值为50
'hao123'.startswith('he') #是不是以什么开头
'号23'.ljust() #左平移
'hao123'.rjust()#右平移
'hellp.tar.gz'.split(".")#以"."切割变成列表
