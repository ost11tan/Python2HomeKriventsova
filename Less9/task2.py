"""Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
 Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл."""

import random
import csv
from typing import Callable
import json
import os


def random_in_csv() -> None:
    with (open('coefficient.csv', "w", encoding="UTF-8") as f):
        csv_write = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        for _ in range(random.randint(MIN_STR, MAX_STR)):
            coefficients = [random.uniform(MIN, MAX) for i in range(3)]
            csv_write.writerow(coefficients)


def print_json(func: Callable):
    file_name = "res.json"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="UTF-8") as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        dict_json = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dict_json['result'] = result
        data.append(dict_json)

        with open(file_name, 'w', encoding="UTF-8") as f1:
            json.dump(data, f1)

    return wrapper


def equation(func: Callable):
    def wrapper(file):
        with open('coefficient.csv', "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            for coefficients in reader:
                if not coefficients == []:
                    # Вопрос!!! что я сделала не так,чт опри генерации строка пустая чередуется со строкой с данными
                    a, b, c = map(float, coefficients)
                    result = func(a, b, c)
                    print(f"Уравнение: {a}x\u00B2 + {b}x + {c} = 0")
                    print(f"Решение: {result}")
                    print()

    return wrapper


@equation
@print_json
def roots(a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return 'Нет рациональных корней'


if __name__ == "__main__":
    MIN = -100
    MAX = 101
    MIN_STR = 100
    MAX_STR = 1000
    random_in_csv()
    roots('coefficient.csv')
