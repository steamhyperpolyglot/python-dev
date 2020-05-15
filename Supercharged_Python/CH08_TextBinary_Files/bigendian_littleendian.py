import struct

with open('junk.dat', 'wb') as f:
    bstr = struct.pack('hhh', 1, 2, 100)
    datalen = f.write(bstr)

with open('junk.dat', 'rb') as f:
    bstr = f.read(struct.calcsize('hhh'))
    a, b, c = struct.unpack('hhh', bstr)
    print(a, b, c)