"""Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""


import os
from pathlib import Path


def rename_group(amount:int,number:int,extension:str,extension_new:str,diapason:list)->None:
    count = 0
    temp=[]
    for _ in range (number):
        temp.append("0")
    numer="".join(temp)

    for file in os.listdir():
        if file.endswith(extension) and count<amount:
            count += 1

            temp=len(str(count))

            numer=numer[:-temp]+f"{count}"
            Path(file).rename(f"{file.split('.')[0][int(diapason[0]):int(diapason[1])]}{numer}.{extension_new}")




if __name__=="__main__":
    amount=int(input("Введите количество файлов,которые хотите переименовать : "))
    number = int(input("Введите количество цифр,которые вы хотите видеть в порядковом номере: "))
    diapazon=input("Введите диапазон через запятую:").split(",")
    extension = input("Введите расширение исходного файла: ")
    extension_new = input("Введите расширение конечного файла: ")
    #print(diapazon)
    
    rename_group(amount,number,extension,extension_new,diapazon)
