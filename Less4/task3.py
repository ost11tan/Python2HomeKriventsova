""""Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление."""


def function(**kwargs)->dict:
    res_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ == None:
            value = str(value)
        res_dict[value] = key
    return res_dict


if __name__=='__main__':
    print(function(first=1,second="слово",third=(1,2,3,4,6,8),fourth={1,2,3,4,6,8},fifth=[10,4,2,3,6,8],sixth=""))


