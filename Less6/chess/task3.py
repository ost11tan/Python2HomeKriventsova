"""Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

def filling_array(n:int)->list:
    list_of_CHES = []
    for i in range(n):
        s=input(f"{i+1}:")
        list_of_CHES.append(str_to_tuple(s))
    return list_of_CHES

def str_to_tuple(s:str)->tuple():
    new=s.split(",")
    for item in range(len(new)):
        new[item]=check(new[item])
    return  int(new[0]),int(new[1])

def check(s:str)->str:
    global COLOMN
    while True:
        tmp=s
        if not tmp.isnumeric() or int(tmp)<1 or int(tmp)>COLOMN:
            s = input(f"{tmp} не число в диапазоне от 1 до {COLOMN}, введите число вместо {tmp} ")
        else:
            break
    return tmp

def chess(arr:list):
    global COLOMN
    list_x=[*[item[0] for item in arr]]
    list_y = [*[item[1] for item in arr]]
    if ort(list_x)==1 and ort(list_y)==1 and diagonal(list_x, list_y)==1:
                return True
    else:
        return False




def ort(arr:list)->bool:
    flag=1
    for i in range(len(arr)):
        temp=arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j]==temp:
                flag=0
                return flag
    return flag
def diagonal(arr_x:list,arr_y:list)->bool:
    flag=1
    for i in range(len(arr_x)):
        for j in range(i + 1, len(arr_x)):
            if abs(arr_x[i] - arr_x[j]) == abs(arr_y[i] - arr_y[j]):
                flag=0
                return flag
    return flag



if __name__ =="__main__":
    LEN = COLOMN=8
    print("Введите координату по горизонтали и координату по вертикали через запятую")
    chess(filling_array(LEN))
