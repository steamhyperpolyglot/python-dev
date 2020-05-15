import struct
from struct import pack, unpack, calcsize

def write_floats(fname, x, y, z):
    with open(fname, 'wb') as f:
        bss = pack('fff', x, y, z)
        f.write(bss)

def read_floats(fname):
    with open(fname, 'rb') as f:
        bss = f.read(calcsize('fff'))
        return unpack('fff', bss)

write_floats('silly.dat', 1, 2, 3.14)
x, y, z = read_floats('silly.dat')
print(x, y, z, sep='   ')