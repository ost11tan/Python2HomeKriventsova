import task17
import task18
import task2
import task3
import task4



task = int(input("Введите номер задания : "))
if task==1:
    task1 = int(input("Введите номер задания (7 или 8): "))
    if task1==7:
        task17.main()
    elif task1==8:
        task18.main()
    else:
        print("Такого задания нет")
elif task==2:
    task2.main()
elif task==3:
    task3.main()
elif task==4:
    task4.main()
else:
    print("Такого задания нет")