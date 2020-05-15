import struct
from struct import pack, unpack, calcsize

def write_rec(fname, name, addr, rating):
    with open(fname, 'wb') as f:
        bname = name.encode('utf-8')
        baddr = addr.encode('utf-8')
        bss = pack('9s10sf', bname, baddr, rating)
        f.write(bss)

def read_rec(fname):
    with open(fname, 'rb') as f:
        bss = f.read(calcsize('9s10sf'))
        bname, baddr, rating = unpack('9s10sf', bss)
        name = bname.decode('utf-8').rstrip('\x00')
        addr = baddr.decode('utf-8').rstrip('\x00')
        return name, addr, rating

write_rec('goofy.dat', 'Cleo', 'Main St.', 5.0)
print(read_rec('goofy.dat'))