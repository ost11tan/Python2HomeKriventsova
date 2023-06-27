#Задание №7
#Погружение в Python | Коллекции
#✔ Пользователь вводит строку текста.
#✔ Подсчитайте сколько раз встречается
#каждая буква в строке без использования
#метода count и с ним.
#✔ Результат сохраните в словаре, где ключ —
#символ, а значение — частота встречи
#символа в строке.
#✔ Обратите внимание на порядок ключей.
#Объясните почему они совпадают
#или не совпадают в ваших решениях


def main():
    data = input("Введите любую строку  : ")

    dict_by_count= {}
    for item in data:
        dict_by_count[item] = data.count(item)

    print(f"Решение через count {dict_by_count}")

    dict_not_count = {}

    for i in data:
        temp=i
        count=0
        for j in range(len(data)):
            if data[j]==temp:
                count+=1
        dict_not_count[i]=count

    print(f"решение без count{dict_not_count}")

