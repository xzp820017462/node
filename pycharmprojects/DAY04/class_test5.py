import sys
import subprocess #subprocess.call ('ls /root', shell=True)
from randpass import randpass

def adduser(username, password, fname):
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (password, username), shell=True)

    user_info = """user information:
用户名: %s
密码: %s  
    """ % (username, password)

    with open(fname, 'a') as fobj:
        fobj.write(user_info)



if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass()
    adduser(username, password, '/tmp/users.txt')

