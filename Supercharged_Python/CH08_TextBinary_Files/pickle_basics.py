import pickle

with open('goo.dat', 'wb') as f:
    pickle.dump([1, 2, 3], f)
    pickle.dump('Hello!', f)
    pickle.dump(3.141592, f)

with open('goo.dat', 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)