

# This program writes three lines of data
# to a file
def main():
    # Open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosophers to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

# Call the main function.
main()
