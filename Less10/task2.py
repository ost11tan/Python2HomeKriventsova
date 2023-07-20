"""Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
class ferse:
    COLOMN=8
    def __init__(self):
        self.list_of_f=self.filling_array()


    def filling_array(self) -> list:
        print("Введите координату по горизонтали и координату по вертикали через запятую")
        list_of_CHES = []
        for i in range(self.COLOMN):
            s = input(f"{i + 1}:")
            list_of_CHES.append(self.str_to_tuple(s))
        return list_of_CHES

    def str_to_tuple(self,s:str)->tuple():
        new=s.split(",")
        for item in range(len(new)):
            new[item]=self.check(new[item])
        return  int(new[0]),int(new[1])

    def check(self,s:str)->str:
        while True:
            tmp=s
            if not tmp.isnumeric() or int(tmp)<1 or int(tmp)>self.COLOMN:
                s = input(f"{tmp} не число в диапазоне от 1 до {self.COLOMN}, введите число вместо {tmp} ")
            else:
                break

        return tmp

    def chess(self):
        list_x=[*[item[0] for item in self.list_of_f]]
        list_y = [*[item[1] for item in self.list_of_f]]
        if self.ort(list_x)==1 and self.ort(list_y)==1 and self.diagonal(list_x, list_y)==1:
                    return True
        else:
            return False



    def ort(self,arr:list)->bool:
        flag=1
        for i in range(len(arr)):
            temp=arr[i]
            for j in range(i + 1, len(arr)):
                if arr[j]==temp:
                    flag=0
                    return flag
        return flag
    def diagonal(self,arr_x:list,arr_y:list)->bool:
        flag=1
        for i in range(len(arr_x)):
            for j in range(i + 1, len(arr_x)):
                if abs(arr_x[i] - arr_x[j]) == abs(arr_y[i] - arr_y[j]):
                    flag=0
                    return flag
        return flag


if __name__ =="__main__":
    ferse_list=ferse()
    print(f"Ферзи не бьют друг друга {ferse_list.chess()}")
