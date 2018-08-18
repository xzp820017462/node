import sys
x = sys.argv[1]
y = sys.argv[2]
def cp_file(x, y):

    #src_fname = '/bin/ls'
    #dst_fname = '/root/ls'
    src_fobj = open(x, 'rb')
    dst_fobj = open(y, 'wb')

    while True:
        data = src_fobj.read(4096)
        if data == b'':
            break
        dst_fobj.write(data)

cp_file(x,y)
#src_fobj.close()
#dst_fobj.close()

















