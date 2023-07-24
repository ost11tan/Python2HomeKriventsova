"""Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя."""


class Arhiv:
    """Строка документации задание 3"""

    __instance = None

    def __init__(self, num: int, text: str, ):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_lst = []
            cls.__instance.text_lst = []
        else:
            cls.__instance.num_lst.append(cls.__instance.num)
            cls.__instance.text_lst.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        """Для пользователя"""
        return f"Текущее значение text {self.text} текущее значение num {self.num},архив text {self.text_lst} " \
               f"архив num {self.num_lst}"

    def __repr__(self):
        """Для программиста"""
        return f"Текущее значение text {self.text} текущее значение num {self.num},архив text {self.text_lst} " \
               f"архив num {self.num_lst}"


if __name__ == "__main__":
    new_a = Arhiv(1, "Какой-то текст")
    print(new_a.num_lst)
    print(new_a.text_lst)

    new_a = Arhiv(2, "7895452")
    print(new_a.num_lst)
    print(new_a.text_lst)
    print(Arhiv.__doc__)
    print(new_a)
    print(repr(new_a))
