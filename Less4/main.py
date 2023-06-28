import task1
import task2
import task3
import task4
"""ВОПРОС!!!
Ранее мы писали в главном файле,при вызове функции из другого файла task1.main
теперь,при выборе task1. автоматически main дает выбрать только в таком виде
Я понимаю,что данное оформление не верно,но не могу сообразить как должно выглядеть
Если в файлах пишу if __name__=='__task1__' ,то не запускается сам файл"""


if __name__=='__main__':
    task = int(input("Введите номер задания : "))
    if task==1:
        if __name__ == '__main__':
            task1
    elif task==2:
        if __name__ == '__main__':
            task2
    elif task==3:
        if __name__ == '__main__':
            task3
    elif task==4:
        if __name__ == '__main__':
            task4
    else:
        print("Такого задания нет")