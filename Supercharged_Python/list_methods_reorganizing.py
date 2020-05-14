# List methods: Reorganizing
def main():
    my_list = []    # Start with empty list
    while True:
        s = input('Enter next name: ')
        if len(s) == 0:
            break
        my_list.append(s)
    my_list.sort()  # Place all elems in order.
    print('Here is the sorted list:')
    for a_word in my_list:
        print(a_word, end=' ')

main()