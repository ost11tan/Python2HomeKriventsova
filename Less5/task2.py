"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def way(str_imput:str)->tuple:
    path=str_imput.split("\\")
    name=str_imput.split("\\")[-1]
    path.pop()
    type=name.split(".")[-1]
    name=name.split(".")[0]
    res=(path,name,type)
    return res




if __name__=="__main__":
    data = input("Введите любую строку  : ")
    print(way(data))