from struct import pack, unpack, calcsize
import struct

def write_num(fname, n):
    with open(fname, 'wb') as f:
        bss = pack('h', n)
        f.write(bss)

def read_num(fname):
    with open(fname, 'rb') as f:
        bss = f.read(calcsize('h'))
        t = struct.unpack('h', bss)
        return t[0]

write_num('silly.dat', 125)
print(read_num('silly.dat'))    # Write the number 125.