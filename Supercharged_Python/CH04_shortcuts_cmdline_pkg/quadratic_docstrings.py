def quad(a, b, c):
    '''
    Quadratic Formula function.

    This function applies the Quadratic Formula 
    to determine the roots of x in a quadratic
    equation of the form ax^2 + bx + c = 0.
    '''
    determin = (b * b - 4 * a * c) ** .5
    x1 = (-b + determin) / (2 * a)
    x2 = (-b - determin) / (2 * a)
    return x1, x2

help(quad)