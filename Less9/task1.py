import json
import csv
from typing import Callable
import os
import random
from functools import wraps


def logger(func: Callable):
    wraps(func)
    file_name = f'{func.__name__}.json'
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

        return result

    return wrapper


def chek_parametr(func: Callable):
    wraps(func)
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT = 1

    def wrapper(number: int, count: int, *args, **kwargs):
        if number > MAX_NUM or number < MIN_NUM:
            number = random.randint(MIN_NUM, MAX_NUM)
        if count > MAX_COUNT or count < MIN_COUNT:
            count = random.randint(MIN_COUNT, MAX_COUNT)
        print(number, count)
        result = func(number, count, *args, **kwargs)

        return result

    return wrapper


def count_f(num: int = 1):
    def deco(func: Callable):
        wraps(func)
        result = []

        def wrapper(*args, **kwargs):
            for i in range(num):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco
@count_f(3)
@chek_parametr
@logger
def gess_number(number: int, count: int) -> Callable[[], None]:
    def gess():
        for i in range(1, count + 1):
            print(f"Попытка №{count}")
            num_input = int(input("Введите число:"))
            if num_input == number:
                print("Вы угадали !")
                break
            elif num_input < number:
                print("Ваше число меньше")
            else:
                print("Ваше число больше")


def get_summ(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == "__main__":
    game = gess_number(25, 4)
    print(game)
