# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Dog:
    def __init__(self, age: int, name: str, purpose: str, wool: str):
        """
        Создание и подготовка к работе объекта "кот"
        :param age: возраст
        :param name: имя
        :param purpose: назначение
        :param wool: шерсть
        Пример:
        >>> kratos = Dog(1, 'kratos', 'friend', 'smooth-haired')
        >>> kratos.age
        1
        >>> kratos.name
        'Kratos'
        >>> kratos.purpose
        'friend'
        >>> kratos.wool
        'smooth-haired'
        """

        self.age = None
        self.name = None
        self.purpose = None
        self.wool = None
        self.init_age(age)
        self.init_name(name)
        self.init_purpose(purpose)
        self.init_wool(wool)

    def init_age(self, age: int):
        """
        Инициализация атрибута age
        :param age: возраст
        :return:  возраст пса
        """
        if not isinstance(age, int):
            raise TypeError('"age" может быть только целым числом (int)')
        if not age > 0:
            raise ValueError('"age" не может быть отрицательным')
        self.age = age

    def init_name(self, name: str):
        """
        Инициализация атрибута name
        :param name: имя
        :return: имя
        """
        if not isinstance(name, str):
            raise TypeError('"name" должен быть типа "str"')
        self.name = name.capitalize()

    def init_purpose(self, purpose: str):
        """
        Инициализация атрибута purpose
        :param purpose: назначение собаки
        :return: назначение собаки
        """
        if not isinstance(purpose, str):
            raise TypeError('"purpose" должен быть типа "str"')
        self.purpose = purpose

    def init_wool(self, wool: str):
        """
        Инициализация атрибута wool
        :param wool: шерсть
        :return: тип шерсть
        """
        if wool not in ('bald', 'smooth-haired', 'medium-haired', 'longhaired'):
            raise ValueError('"wool" может быть только: "bald", '
                             '"smooth-haired", "medium-haired", "longhaired" ')
        self.wool = wool

    def add_age(self, increase_age: int):
        """
        Увеличение возраста на заданную величину
        :param increase_age: на сколько лет увеличиваем возраст
        :return: новый текущий возраст
        Примеры:
        >>> kratos = Dog(1, 'kratos', 'friend', 'smooth - haired')
        >>> kratos.add_age(10)
        >>> kratos.age
        11
        """
        if increase_age <= 0:
            raise ValueError('"increase_age" должен быть больше нуля')
        self.age += increase_age

    def __repr__(self) -> str:
        """
        Метод repr для создания копии объекта  класса
        :return: объект класса Cat со всеми атрибутами
        """
        return f"Dog({self.age}, {self.name}, {self.purpose}, {self.wool})"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    # dog1 = Dog(1, 'kratos', 'friend', 'smooth-haired')
    # print(dog1.name)
    # print(dog1.age)
    # dog1.add_age(5)
    # print(dog1.age)
    # print(dog1.wool)