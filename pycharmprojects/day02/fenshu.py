a = "优秀"
b = "好"
c = "良"
d = "及格"


point = input('输入一个成绩')
point = int(point)
if point >= 90:
    print(a)
elif point <90 and point >=80: #elif 90<point<=80 跟我这个是一样的
    print(b)
elif point <80 and point >=70:# elif 80<point<=70
    print(c)
elif point <70 and point >=60 : #elif 70<point<=60
    print(d)
else:
    print("你还仍需努力")


