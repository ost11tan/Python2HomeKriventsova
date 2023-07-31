class UserException(Exception):
    pass

class UserValueError(UserException):
    def __init__(self, value,COLOMN):
        self.value = value
        self.COLOMN=COLOMN

    def __str__(self):
        if not self.value.isnumeric():
            text=f"Значение {self.value} должно быть числом!"
        elif not int(self.value):
            text =f"Значение {self.value} должно быть целочисленным!"
        elif int(self.value) < 1:
            text =f"Значение {self.value} должно быть >0"
        elif int(self.value) > self.COLOMN:
            text =f"Значение {self.value} должно быть <= {self.COLOMN} "
        return text


class UserFibError(UserException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Введенное значение {self.value} не является целым положительным числом"


