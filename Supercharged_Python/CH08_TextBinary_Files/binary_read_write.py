with open('my.dat', 'wb') as f:
    f.write(b'\x01\x02\x03\x10')

with open('my.dat', 'rb') as f:
    bss = f.read()
    for i in bss:
        print(i, end=' ')