# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def correctness_check():
    num = int(input("Введите число: "))
    if 0 < num < 100000:
        if num == 1:
            print("Число 1 не является ни простым ни составным")
        else:
            prime_number(num)


    else:
        print("Введите число больше нуля и меньше ста тысяч")
        correctness_check()

def prime_number(numer):
    flag=0
    for i in range(2, numer):
        if numer % i == 0:
            flag=1
    if flag==1:
        print("Число является составным")
    else:
        print("Число является простым ")

correctness_check()