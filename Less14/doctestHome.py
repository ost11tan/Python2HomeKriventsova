from calendar import is_real_date
from calendar import _is_leap_year
import dicthome


def test_add():
    """
    >>> date="11.5.1995"
    >>> date
    '11.5.1995'

    >>> is_real_date(date)
    True

    >>> _is_leap_year(2004)
    True

    >>> _is_leap_year(2200)
    False
    """

def test_dict():
    """
    >>> names=["Иван","Андрей","Кирилл"]
    >>> rate=[26,586,30]
    >>> bonus = ["11.64%", "10.25%", "4.9%"]
    >>> dicthome.bonuses(names,rate,bonus,3)
    {'Иван': 302.64, 'Андрей': 6006.5, 'Кирилл': 147.0}

    """

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

