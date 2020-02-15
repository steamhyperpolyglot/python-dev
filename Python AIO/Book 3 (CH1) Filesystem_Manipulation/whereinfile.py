with open('names.txt', encoding='utf-8', errors='ignore') as f:
    # Read first line to get started.
    print(f.tell())

    
    one_line = f.readline()
    # keep reading one line at a time until there are no more.
    while one_line:
        print(one_line[:-1], f.tell())
        one_line = f.readline()
