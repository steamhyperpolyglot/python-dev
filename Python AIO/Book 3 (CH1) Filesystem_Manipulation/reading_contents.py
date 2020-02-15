with open('quotes.txt') as f:
    # content = f.readlines()   # <- This reads the entire file
    # content = f.readline()  # <- This reads a single line
    # print(content)
    # f.close()

    # Reads in all lines first, then loops through.
    for one_line in enumerate(f.readlines()):
        # If counter is even number, print with no extra newline
        if one_line[0] % 2 == 0:
            print(one_line[1], end='')
        # otherwise, print a couple spaces and an extra newline
        else:
            print('  ' + one_line[1])
