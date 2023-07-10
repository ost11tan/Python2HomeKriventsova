"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from task1 import is_real_date

def imput_date()->str:
    date=input('Введите дату в формате DD.MM.YYYY: ')
    return date

if __name__=="__main__":
    print(is_real_date(imput_date()))


