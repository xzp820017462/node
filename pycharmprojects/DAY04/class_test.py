"""
1.思考一下.程序的运行场景
2.构思程序的结构,把每一个功能,写成一个函数
3·编写主程序代码,把这些函数串联起来,
4·编写具体的函数代码部分,
"""
import os

def get_fname(x): #获得文件名

    while True :
        fname = input("file name")
      #  if os.path.exists(fname):
      #      print('%s already exits. Try again')
      #      continue
      #  else:
      #      break
        if not os.path.exists(fname):
            break
        print('%s already exits. Try again' % fname)
        return fname


def get_content():
    content = []
    print("请输入正文,end结束")
    while True :  #不知道用户用几行数据
        line = input(">")
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname,content):
    with open(fname, 'wb') as fobj:
        fobj.writelines(content)
if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    ['%s\n' % line for line in content]#我这里有个列表.列表里有123.有hello.content = ['123', 'hello'] ['%s\n' % line for line in content ]
    wfile(fname,content)