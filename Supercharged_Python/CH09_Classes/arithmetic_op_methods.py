import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        '''Return a point containing self + other.'''
        newx = self.x + other.x
        newy = self.y + other.y
        return Point(newx, newy)
    
    def __sub__(self, other):
        '''Return the distance between points.'''
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** .5
    
    def __mul__(self, other):
        if type(other) == Point:
            newx = self.x * other.x
            newy = self.y * other.y
            return Point(newx, newy)
        elif isinstance(other, (int, float)):
            newx = self.x * other
            newy = self.y * other
            return Point(newx, newy)
        else:
            return NotImplemented

    def __neg__(self):
        newx = -self.x
        newy = -self.y
        return Point(newx, newy)

    def __trunc__(self):
        newx = self.x.__trunc__()
        newy = self.y.__trunc__()

        return Point(newx, newy)

    def __rmul__(self, other):
        '''Return point * a scalar number, n'''
        if isinstance(other, (int, float)):
            newx = self.x * other
            newy = self.y * other
            return Point(newx, newy)
        else:
            return NotImplemented
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other.y
        return self

    def __int__(self):
        return Point(int(self.x), int(self.y))
    
    def __float__(self):
        return Point(float(self.x), float(self.y))

pt1 = Point(10, 15)
pt2 = Point(0, 5)
x = pt1 - pt2

print('pt1       = (', pt1.x, ', ', pt1.y, ')')
print('pt2       = (', pt2.x, ', ', pt2.y, ')')
print('\npt1 - pt2 = (', x, ')')

# multiplication = math.trunc(pt1 * 2.25)
multiplicaton = pt1 * pt2

print('multiplication = (', multiplicaton.x, ', ', multiplicaton.y, ')')

unaryNegation = -pt1

print('unary negation = (', unaryNegation.x, ', ', unaryNegation.y, ')')