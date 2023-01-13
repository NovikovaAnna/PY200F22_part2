import doctest


class Education:
    def __init__(self, studing_age: int, degree: str, specialization: str):
        """
        Создание и подготовка к работе объекта  "образование"
        :param studing_age: срок обучения
        :param degree: степень
        :param specialization:  специализация
        Пример:
        >>> edcation_1 = Education(5, 'specialist', 'economy')
        >>> education_1.studing_age
        5u
        >>> education_1.degree
        'specialist'
        >>> education_1.specialization
        'economy'
        """

        self.studing_age = None
        self.degree = None
        self.specialization = None
        self.init_studing_age(studing_age)
        self.init_degree(degree)
        self.init_specialization(specialization)

    def init_studing_age(self, studing_age: int):
        """
        Инициализация атрибута studing_age
        :param studing_age: срок обучения
        :return:  срок обучения
        """
        if not isinstance(studing_age, int):
            raise TypeError('"studing_age" может быть только целым числом (int)')
        if not studing_age > 0:
            raise ValueError('"studing_age" не может быть отрицательным')
        self.studing_age = studing_age

    def init_degree(self, degree: str):
        """
        Инициализация атрибута degree
        :param degree: степень
        :return: степень
        """
        if not isinstance(degree, str):
            raise TypeError('"degree" должен быть типа "str"')
        self.degree = degree.capitalize()

    def init_specialization(self, specialization: str):
        """
        Инициализация атрибута specialization
        :param specialization: специиализация
        :return: специализация
        """
        if not isinstance(specialization, str):
            raise TypeError('"specialization" должен быть типа "str"')
        self.specialization = specialization.capitalize()

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()