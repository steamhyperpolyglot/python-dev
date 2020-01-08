# This program has a recursive function

def message(times):
    if times > 0:
        print('This is a recursive function.')
        message(times - 1)

def main():
    message(5)

# Call the main function
main()