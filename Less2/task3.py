#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions
from fractions import Fraction
def function():
    print("Введите первое число ")
    st_num1 = read_num()
    num1=int(st_num1[0])/int(st_num1[1])
    f1=fractions.Fraction(int(st_num1[0]),int(st_num1[1]))

    print("Введите второе число ")
    st_num2 = read_num()
    num2=int(st_num2[0])/int(st_num2[1])
    f2 = fractions.Fraction(int(st_num2[0]), int(st_num2[1]))



    print("Сумма дробей равна "+str(num1+num2))
    print("Число,выданное модулем fractions "+str(f1+f2))
    print("Произведение дробей равно "+str(num1*num2))
    print("Число,выданное модулем fractions "+str(f1*f2))
def read_num():
    a=0
    b=0
    str_num = input("Введите в формате “a/b”: ")
    str_num=str_num.split("/")
    if str_num[0].isdigit():
        a=int(str_num[0])
    else:
        print("Вы точно ввели число?")
        read_num()

    if str_num[1].isdigit() and int(str_num[1])!=0:
        b = int(str_num[1])
    elif str_num[1].isdigit() and int(str_num[1])==0:
        print("Деление на ноль!!!")
        read_num()
    else:
        print("Вы точно ввели число?")
        read_num()

    return str_num #изначально строка выглядела как return a/b
    #и функция сразу возвращала число,а не строку
    #данное изменение для того,чтоб не повторяться и попробовать модуль Fraction
