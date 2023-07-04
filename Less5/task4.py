"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""
def febb(amount:int):
    a, b = 0, 1
    for __ in range(amount):
        yield a
        a, b = b, a + b


if __name__ =="__main__":
    LEN = int(input("Введите количество элементов : "))
    if LEN>0:
        for item in febb(LEN):
            print(item, end=" ")
    else:
        print(("Введите количество элементов >0 "))