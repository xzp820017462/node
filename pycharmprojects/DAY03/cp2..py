import sys
def copy_file(l, q):
    src_file=open(sys.argv[1], 'rb')
    dst_file=open(sys.argv[2], 'wb')

    while True:
        data = src_file.read(4096)
        if data == b'':
            break
        dst_file.write(data)

copy_file(sys.argv[1], sys.argv[2])
            
