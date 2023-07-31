"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


from error import UserFibError
def febb(amount:int):
    a, b = 0, 1
    for __ in range(amount):
        yield a
        a, b = b, a + b


if __name__ =="__main__":
    while True:
        LEN = input("Введите количество элементов : ")
        if not LEN.isnumeric() or int(LEN)==0:
            raise UserFibError(LEN)
        else:
            for item in febb(int(LEN)):
                print(item, end=" ")
                break
