from decimal import Decimal

class Money():

    default_curr = 'USD'

    exch_dict = {
        'USDCAD': Decimal('0.75'), 'USDEUR': Decimal('1.16'),
        'CADUSD': Decimal('1.33'), 'CADEUR': Decimal('1.54'),
        'EURUSD': Decimal('0.86'), 'EURCAD': Decimal('0.65')
    }

    def __init__(self, v = '0', units = ''):
        self.dec_amount = Decimal(v)
        if not units:
            self.units = Money.default_curr
        else:
            self.units = units

    def __str__(self):
        s = str(self.dec_amount) + ' ' + self.units
        return s
    
    def __repr__(self):
        s = ('Money(' + str(self.dec_amount) + ' ' + self.units + ')')
    
    def __add__(self, other):
        '''Money add function.
        Supports two Money objects added together; if the
        second has a different currency unit, then exchange
        rate must be applied before adding the two amounts
        togther. Applying rounding of 2.
        '''

        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m1 = self.dec_amount
            m2 = other.dec_amount * r
            m = Money(m1 + m2, self.units)
        else:
            m = Money(self.dec_amount + other.dec_amount, self.units)
        
        m.dec_amount = round(m.dec_amount, 2)
        return m

# m1 = Money('0.10', 'CAD')
# print(m1)
# m1
us_m = Money('1' ,'USD')
ca_m = Money('1', 'CAD')
print(us_m + ca_m)