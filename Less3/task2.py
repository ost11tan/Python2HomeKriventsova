#Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

def main():

    elements=[1,6,8,6,3,5,9,99,6,2345,2,1,6,8,"dfg",5,"hhf","a","a","a",1,3,2,6,6,6,"b","a","b"]
    res=[]
    print(f"Исходный список: {elements}")

    DUBL=2

    for item in set(elements):
        if elements.count(item)>=DUBL:
            res.append(item)

    print(f"Список дубликатов: {res}")
