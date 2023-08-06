from calendar import is_real_date
from calendar import _is_leap_year
import dicthome
import pytest



def test_add():
    date = "11.5.1995"
    assert date == '11.5.1995'


def test_real():
    date = "11.5.1995"
    assert is_real_date(date) == True


def test_is_leap_year1():
    assert _is_leap_year(2004) == True


def test_is_leap_year():
    assert _is_leap_year(2200) == False


def test_dict():
    names=["Иван","Андрей","Кирилл"]
    rate=[26,586,30]
    bonus = ["11.64%", "10.25%", "4.9%"]
    assert (dicthome.bonuses(names,rate,bonus,3),{'Иван': 302.64, 'Андрей': 6006.5, 'Кирилл': 147.0})

if __name__ == '__main__':

    pytest.main()
