# Specify the file to copy.
file_to_copy = 'happy_pickle.png'
#  Create new file name with _copy before the extension
name_parts = file_to_copy.split('.')
new_file = name_parts[0] + '_copy.' + name_parts[1]
# Open the original file as read-only binary.
with open(file_to_copy, 'rb') as original_file:
    # Create or open file to copy into.
    with open(new_file, 'wb') as copy_to:
        # Grab a chunk of original file (4MB).
        chunk = original_file.read(4096)
        # Loop through until no more chunks.
        while len(chunk) > 0:
            copy_to.write(chunk)
            # Make sure you read next chunk in this loop.
            chunk = original_file.read(4096)

print('Done!')
