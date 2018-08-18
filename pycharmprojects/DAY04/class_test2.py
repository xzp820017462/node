import os
counter = 0
def get_fname():
    while counter < 3:
        fname = input("file names: ")
        if not os.path.exists(fname):
            break
        print('%s,file exits,please try again' % fname)
    return fname

def get_content(): #要获得很多的数据,我们要先创建一个列表,然后在列表里面安放数据
    content = []
    while True : #因为不知道用户要输入多少行数据,所以我们要让用户自己决定
        print("请输入正文,end结束")
        line = input(">")
        content.append(line) #把所有输入的数据添加至content的空列表里,
        if line == "end":
            break
    return content


#以上输入数据和读取文件名已经完成,剩下的就是把数据导入进路径下的文件
def wfile(fname,content):#这边因为要导入数据,必须要两个参数.一个是文件名.一个是数据内容
    with open(fname, 'wb' ) as ofbj:
        ofbj.writelines(content) #因为是列表,里面数据要一行一行列出.所以我们必须要进行writelines





