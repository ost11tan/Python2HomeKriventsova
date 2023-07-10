"""Задача с семинара"""

MIN_DATE=1
MAX_YEAR=9999
MAX_MONTH=12
MAX_DAY=1

def is_real_date(date:str)->bool:
    day,month,year=map(int,date.split('.'))

    if not (MIN_DATE<= year<=MAX_YEAR and MIN_DATE<=month<=MAX_MONTH and MIN_DATE<=day<=MAX_DAY):
        return False

    if not (month in (4,6,9,11) and day <=30):
        return False

    if not (month==2 and _is_leap_year(year) and day==29):
        return False

    if not (month==2 and _is_leap_year(year) and day==28):
        return False

    return True

def _is_leap_year(year:int)->bool:
    return  year%4==0 and year%100==0 and year%400==0


if __name__ =="__main__":
    print(is_real_date("21.11.2012"))
