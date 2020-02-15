try:
    # Open file that's in the same folder
    thefile = open('people.csv')
except FileNotFoundError:
    print("Sorry, I don't see a file name people.csv here")
except Exception as e:
    print(e)
else:
    # File must be open by now if we got here
    print('\n')     # Print a blank line.
    # Print each line from the file.
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success!")
