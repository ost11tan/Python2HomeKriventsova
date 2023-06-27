#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re
def main():

    #Попытка вставить с  клавиатуры из буфера обмена,но столкнулась с проблемой "/n" , в строку сохранялась только первая строка,поэтому удалила все \n
    # текст для вставки в файле text.txt
    #data_tmp= input("Введите любую статью из википедии  : ").split("\n")
    #data_tmp1=""
   # for i in range(len(data_tmp)):
    #    data_tmp1=data_tmp1+data_tmp[i]
     #   data=data_tmp1.lower()
    #print(f"строка {data}")

    AMOUNT=10
    data_tmp = input("Введите любую статью из википедии  : ")
    data=data_tmp.lower()

    data = re.sub(r'[^\w\s]',' ', data)

    elements=data.split(" ")

    arr_cortage=[]

    for item in set(elements):
        arr_cortage.append((item,elements.count(item)))

    arr_cortage.sort(key=lambda a: a[1])
    arr_cortage.pop()
    arr_cortage.reverse()
    for i in range(AMOUNT):
        print(arr_cortage[i])




