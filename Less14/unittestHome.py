from calendar import is_real_date
from calendar import _is_leap_year
import dicthome
import unittest


class TestCalendar(unittest.TestCase):
    def test_add(self):
        date = "11.5.1995"
        self.assertEqual(date, '11.5.1995')

    def test_real(self):
        date = "11.5.1995"
        self.assertTrue(is_real_date(date))

    def test_is_leap_year1(self):
        self.assertTrue(_is_leap_year(2004))

    def test_is_leap_year(self):
        self.assertFalse(_is_leap_year(2200))


class TestDict(unittest.TestCase):
    def test_dict():
        names = ["Иван", "Андрей", "Кирилл"]
        rate = [26, 586, 30]
        bonus = ["11.64%", "10.25%", "4.9%"]
        dict_res = dicthome.bonuses(names, rate, bonus, 3)
        self.assertEqual(dict_res, {'Иван': 302.64, 'Андрей': 6006.5, 'Кирилл': 147.0})


if __name__ == '__main__':
    unittest.main()
