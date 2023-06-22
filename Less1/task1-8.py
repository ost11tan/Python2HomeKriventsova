#Задание №8
#Нарисовать в консоли ёлку спросив
#у пользователя количество рядов.

row = int(input("Введите количество рядов: "))
list=["*"]
list2=[]
for i in range(1, row+1):
    list2.append(" ")
print(list2+list)
if row>1:
    for i in range(1, row+1) :
        list.append("*")
        list.append("*")
        list2.remove(" ")
        print(list2+list)
