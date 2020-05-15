import os

with open('sample.txt', 'r') as f:
    lst = f.readlines()
    for thing in lst:
        print(thing, end='')