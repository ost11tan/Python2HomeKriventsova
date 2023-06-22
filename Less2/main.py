import task1
import task2
import task3



task = int(input("Введите номер задания : "))
if task==1:
    task1.main()
elif task==2:
    task2.dec_to_hex()
elif task==3:
    task3.function()
else:
    print("Такого задания нет")