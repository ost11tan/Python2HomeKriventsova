# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def dec_to_hex():
    dec_num = input("Введите целое десятичное число : ")
    rev_hex = ""
    base_of_sys = int(input("Введите основание системы,в которую хотите перевести (16) "))
    if dec_num.isdecimal():

        dec_num = int(dec_num)
        print("Pезультат встроенной функции: " + hex(dec_num))
        while dec_num > base_of_sys:
            to_list = dec_num % base_of_sys
            dec_num = int(dec_num / base_of_sys)
            rev_hex = overwriting(to_list, rev_hex)

        rev_hex = overwriting(dec_num, rev_hex)
        res = ''.join(reversed(rev_hex))

        print("У нас получилось: 0x" + res)




    else:
        print("Число не является целым десятичным! ")
        dec_to_hex()


def num_to_letter(numer):
    if numer == 10:
        letter = "A"
    elif numer == 11:
        letter = "B"
    elif numer == 12:
        letter = "C"
    elif numer == 13:
        letter = "D"
    elif numer == 14:
        letter = "E"
    else:
        letter = "F"

    return letter


def overwriting(to_list, stroka):
    if to_list > 9:
        stroka = stroka + num_to_letter(to_list)
    else:
        stroka = stroka + str(to_list)
    return stroka



