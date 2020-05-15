import shelve
nums = shelve.open('numdb')

nums['pi'] = (3.14192, False)
nums['phi'] = (2.1828, False)
nums['perfect'] = (6, True)
nums.close()

nums = shelve.open('numdb')
for thing in nums:
    print(thing)