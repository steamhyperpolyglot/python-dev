class Point:
    big_prime_1 = 1200556037
    big_prime_2 = 2444555677

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = str(self.x) + ', '
        s += str(self.y)
        return s
    
    