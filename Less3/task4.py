#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def main():
    volume= int(input('Количество всех вещей : '))
    max_mass = int(input('Максимальная грузоподьемность : '))


    backpack = dict()

    for i in range(volume):
        key = input('введите вещь: ')
        value =mass_chek()

        backpack[key] = value




    count=0

    for key, value in backpack.items():
        count = count + value
        if count<=max_mass:
            print(key)
        else:
            count = count - value



def mass_chek():
    while True:
        mass = input("Введите массу: ")
        if not mass.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            mass=int(mass)
            break
    return mass


