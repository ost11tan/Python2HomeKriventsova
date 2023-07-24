"""Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""

from time import time


class My_str(str):
    """Строка документации задание 3"""

    def __new__(cls, value: str, autor_name: str):
        instance = super().__new__(cls, value)
        instance.autor_name = autor_name
        instance.time = time()
        print(f"class {cls} created")
        return instance

    #def __str__(self):
    #    """Для пользователя"""
    #   return f"Автор:{self.autor_name}  время:{self.time} текст:{self}"

    def __repr__(self):
        """Для программиста"""
        return f"Автор:{self.autor_name}  время:{self.time} текст:{self}"

if __name__ == "__main__":
    new_str = My_str("ляляля", "я")
    print(new_str.autor_name)
    print(new_str.time)
    #print(help(My_str))
    print(My_str.__doc__)
    print(repr(new_str))
