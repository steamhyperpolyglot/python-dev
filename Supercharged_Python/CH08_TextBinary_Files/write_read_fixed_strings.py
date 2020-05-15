from struct import pack, unpack, calcsize
import struct

def write_fixed_str(fname, n, s):
    with open(fname, 'wb') as f:
        bss = pack(str(n) + 's', s.encode('utf-8'))
        f.write(bss)

def read_fixed_str(fname, n):
    with open(fname, 'rb') as f:
        bss = f.read(n)
        return bss.decode('utf-8')

write_fixed_str('king.d', 13, "I'm Henry the VIII I am!")
print(read_fixed_str('king.d', 13))