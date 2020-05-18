# Place Money class definition here or import it.
from money import Money


def money_calc():
    '''
    Money addition calculator.
    Prompt for a series of Money objects until empty
    string is entered; then print results of the
    running total.
    '''
    n = 0
    while True:
        s = input('Enter money value: ')
        s = s.strip()
        if not s:
            break
        a_list = s.split()  # Split into amt, units.
        d = a_list[0]
        if len(a_list) > 1:
            m = Money(d, a_list[1])
        else:
            m = Money(d)
        if n == 0:
            amt = m
            Money.default_curr = m.units
        else:
            amt += m
        n += 1
    print('Total is', amt)


money_calc()
