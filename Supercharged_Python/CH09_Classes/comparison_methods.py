class Dog:
    def __init__(self, d):
        self.d = d
    
    def __eq__(self, other):
        '''Implementation of ==; provides != for free.'''
        return self.d == other.d
    
    def __lt__(self, other):
        '''
        Less than (<). This method much support comparisons to 
        objects of the same class, as well as to numbers.
        '''
        if type(other) == Dog:
            return self.d < other.d
        else:
            return self.d < other
    
    def __le__(self, other):
        '''Implementation of <=; provides >= for free.'''
        return self.d <= other.d
    
    def __gt__(self, other):
        '''
        Greater than (>). This method provides a less-than comparison
        through Rules of Symmetry.
        if a > b, then b < a.
        '''
        if type(other) == Dog:
            return self.d > other.d
        else:
            return self.d > other
    
    # Defining __repr__ also gets us __str__.
    def __repr__(self):
        return "Dog(" + str(self.d) + ")"

d1, d5, d10 = Dog(1), Dog(5), Dog(10)
a_list = [50, d5, 100, d1, -20, d10, 3]
print('Before sorting...')
print(a_list)
a_list.sort()
print('\nAfter sorting...')
print(a_list)
