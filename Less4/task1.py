"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""


def function(data:list[str])->list[str]:
    temp = []
    for i in range(len(data)):
        if data[i][-1:]=="s" and len(data[i])!=1:
            temp.append(data[i])
            data[i] = None

    for i in range (len(temp)):
        data.append(temp[i])

    return data


if __name__=='__main__':
    new_data=["s", "task", "song", "parts", "friends", "374586940","qwertys","123"]
    print(function(new_data))