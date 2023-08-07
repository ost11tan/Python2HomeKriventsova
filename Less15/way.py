"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""
import logging
import argparse

logging.basicConfig(level=logging.INFO, filename='home.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def Parser():
    parser = argparse.ArgumentParser(description='Введите путь')
    parser.add_argument('-p')
    args = parser.parse_args()
    return way(args.p)

def way(str_imput:str)->tuple:
    path=str_imput.split("\\")
    name=str_imput.split("\\")[-1]
    path.pop()
    type=name.split(".")[-1]
    name=name.split(".")[0]
    res=(path,name,type)
    logger.info(f"Таков путь {res[0]} имя {res[1]}  расширение {res[2]}  ")
    return res




if __name__=="__main__":
    print(Parser())