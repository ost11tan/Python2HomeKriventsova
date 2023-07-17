import json
import csv
from typing import Callable


def logger(func: Callable):
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
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT = 1

    def wrapper(number: int, count: int, *args, **kwargs):
        if number > MAX_NUM or number < MIN_NUM:
            number = randint(MIN_NUM, MAX_NUM)
        if count > MAX_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)
        print(number, count)
        result = func(number, count, *args, **kwargs)

        return result

    return wrapper
