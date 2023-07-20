"""Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass





class Fish(Animal):

    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        super().__init__(name)
        self.long = long

    def get_info_fish(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-глубуководная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

        def show_spec(self):
            return self.length * 2

class Fabric():
    def new_animal(self, animal_type: str, *args, **kwargs):
        animal_new =self.get_maker(animal_type)
        return animal_new(*args, **kwargs)

    def get_maker(self, animal_type: str):
        types = {'Птица': Bird, 'Рыбка': Fish}
        return types[animal_type]


if __name__ == "__main__":

    """fish1 = Fish('123', 50)
    bird1 = Bird('123', 10)
    animal_list = [fish1, bird1]
    for animal in animal_list:
        print(animal.show_spec())


    print(fish1.get_info_fish())
    print(bird1.show_spec())"""

    fabric = Fabric()
    animal_from_fabric = fabric.new_animal('Рыбка','Какая-то птичка', 3)
    print(animal_from_fabric.get_info_fish())
