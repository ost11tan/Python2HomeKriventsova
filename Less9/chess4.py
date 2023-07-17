"""Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки"""


from chess3 import chess
from chess3 import ort
from chess3 import diagonal
import random

def rand_list(n:int)->tuple:
    global COLOMN
    list_of_x = []
    list_of_x.append(random.randint(1, COLOMN))
    list_of_y = []
    list_of_y.append(random.randint(1, COLOMN))
    for i in range(1,n):
        while True:
            list_of_x.append(random.randint(1, COLOMN))
            list_of_y.append(random.randint(1, COLOMN))
            #print(list_of_x,list_of_y)
            if not (ort(list_of_x) == 1 and ort(list_of_y) == 1 ):
                list_of_x.pop()
                list_of_y.pop()
            else:
                break
    return (list_of_x,list_of_y)

def chek_d()->tuple:
    while True:
        list_x, list_y = rand_list(LEN)[0],rand_list(LEN)[1]
        if not (diagonal(list_x,list_y)==1):
            flag=0
        else:
            break
    return (list_x,list_y)


def to_tuple()->tuple:
    tmp=chek_d()
    list_x, list_y = tmp[0], tmp[1]
    tuple_chess=((list_x[i],list_y[i]) for i in range(len(list_x)) )
    return tuple_chess

def counter(n):
    count=1
    while count<=n:
        print(f"Комбинация {count}")
        print(*to_tuple())
        count+=1

if __name__ =="__main__":
    LEN = COLOMN =8
    COUNTER=4
    counter(COUNTER)
