import os

while True:
    try:
        fname = input('Enter file name: ')
        if not fname:   #Quit on empty string
            break
        f = open(fname) # Attempt file open here.
        print(f.read())
        f.close()
        break
    except FileNotFoundError:
        print('File could not be found. Re-enter.')