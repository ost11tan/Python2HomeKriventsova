MIN_DATE = 1
MAX_YEAR = 9999
MAX_MONTH = 12
MAX_DAY = 31


def is_real_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if not (MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY):
        return True

    if not (month in (4, 6, 9, 11) and day <= 30):
        return True

    if not (month == 2 and _is_leap_year(year) and day == 29):
        return True

    if not (month == 2 and _is_leap_year(year) and day == 28):
        return True

    return False


def _is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        text = True
    elif year % 100 == 0:
        text = False
    elif year % 4 == 0:
        text = True
    else:
        text = False

    return text

    # year % 4 == 0 or  and year % 100 == 0 and year % 400 == 0 Функция рабботает непрвильно!!!
    # игнорирует 2004 и остальные стандартные случаи


if __name__ == "__main__":
    print(is_real_date("11.01.2021"))
