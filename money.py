"""This script implements Money class."""
import json
import requests


class Money:
    """Represent money in various currencies."""

    def __init__(self, amount, curr='BYN'):
        """Initialize an amount in given currency."""
        self.amount = amount
        self.curr = curr

    def __add__(self, other):
        """Redefine __add__."""
        other = other.converted_to(self.curr)
        summa = self.amount + other.amount
        return Money(summa, self.curr)

    def __radd__(self, other):
        """Redefine __radd__."""
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __mul__(self, other):
        """Redefine __mul__."""
        if isinstance(other, Money):
            result = self.amount * other.amount
            return Money(result, self.curr)
        elif isinstance(other, int):
            result = other * self.amount
            return Money(result, self.curr)

    def __rmul__(self, other):
        """Redefine __rmul__."""
        result = other * self.amount
        return Money(result, self.curr)

    def __str__(self):
        """Define str representation of the obj."""
        return '{} {}'.format(round(self.amount, 2), self.curr)

    def __repr__(self):
        """Define str representation of the obj."""
        return '{} {}'.format(round(self.amount, 2), self.curr)

    def __to_byn(self):
        """Convert to BYN."""
        if self.curr == 'BYN':
            return self
        req1 = 'http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2' \
               .format(self.curr)
        resp = requests.get(req1)
        assert resp.ok
        resp_dct = json.loads(resp.text)
        rate = resp_dct['Cur_OfficialRate']
        total = self.amount * rate
        return Money(total, 'BYN')

    def converted_to(self, other_curr):
        """Convert the money to different currencies."""
        if self.curr == other_curr:
            return self
        if other_curr == 'BYN':
            return self.__to_byn()
        req = 'http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2' \
              .format(other_curr)
        resp = requests.get(req)
        assert resp.ok
        resp_dct = json.loads(resp.text)
        rate = resp_dct['Cur_OfficialRate']
        if self.curr != 'BYN':
            amount_in_BYN = self.__to_byn().amount
        else:
            amount_in_BYN = self.amount
        result = amount_in_BYN / rate
        return Money(result, other_curr)


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + x + y)
print(sum([x, y, z]))
print(sum([10 * x, y * 10, z]))
