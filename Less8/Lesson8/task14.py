"""Задание №
+Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
+Дополните id до 10 цифр незначащими нулями.
+В именах первую букву сделайте прописной.
+Добавьте поле хеш на основе имени и идентификатора.
+Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
+Имя исходного и конечного файлов передавайте как аргументы
функции."""

import json
import csv

def func(csv_file,json_file):
    with (open(csv_file, "r", encoding="UTF-8") as csv_f):
        csv_file = [*csv.reader(csv_f)]
        key_id,key_level,key_name=csv_file[0]

        temp=[]
        for _ in range(NUMBER):
            temp.append("0")
        num = "".join(temp)

        json_list=[{key_id:to_10_Nulls(csv_file[i][0],num),key_level:csv_file[i][1] , key_name:csv_file[i][2].lower(),
                    'hash': hash(csv_file[i][0]+csv_file[i][2])} for i in range (1,len(csv_file))]
        #print(json_list)
    with (open(json_file, "w", encoding="UTF-8", newline='') as json_f):
        json.dump(json_list, json_f, ensure_ascii=False, indent=2)

def to_10_Nulls(id:str,num:str)->str:
    temp=len(id)
    num = num[:-temp] + f"{id}"
    return num


if __name__=='__main__':
    NUMBER=10
    func('names.csv','new_json.json')