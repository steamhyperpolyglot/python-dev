import struct
from struct import pack, unpack, calcsize

def write_var_str(fname, s):
    with open(fname, 'wb') as f:
        n = len(s)
        fmt = 'h' + str(n) + 's'
        bss = pack(fmt, n, s.encode('utf-8'))
        f.write(bss)

def read_var_str(fname):
    with open(fname, 'rb') as f:
        bss = f.read(calcsize('h'))
        n = unpack('h', bss)[0]
        bss = f.read(n)
        return bss.decode('utf-8')

write_var_str('silly.dat', "I'm Henry the VIII I am!")
print(read_var_str('silly.dat'))