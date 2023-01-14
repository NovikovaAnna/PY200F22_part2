import doctest


class Vag_car:
    def __init__(self, brand: str, age: int, car_milage: int, condition: str):
        """
        Создание и подготовка к работе объекта  "автомобиль"
        :param brand: марка автомобиля
        :param age:  возраст
        :param car_milage: пробег
        :param condition:  состояние
        Пример:
        >>> audi_q3 = Vag_car(audi, 10, 166700, 'non_broken')
        >>> audi_q3.brand
        audi
        >>> audi_q3.age
        10
        >>> audi_q3.car_milage
        166700
        >>> audi_q3.condition
        'non_broken'
        """

        self.brand = None
        self.age = None
        self.car_milage = None
        self.condition = None
        self.init_brand(brand)
        self.init_age(age)
        self.init_car_milage(car_milage)
        self.init_condition(condition)

    def init_brand(self, brand: str):
        """
        Инициализация атрибута brand
        :param brand: марка автомобиля
        :return:  марка автомобиля
        """
        if not isinstance(brand, str):
            raise TypeError("'brand' может быть только VAG('Volkswagen','Audi', 'Seat', 'Skoda',"
                            " 'Bugatti', 'Man', 'Lamborghini', 'Ducati', 'Skania', 'Porsche', 'Bentley')")
        if brand not in ('Volkswagen','Audi', 'Seat', 'Skoda',
                        'Bugatti', 'Man', 'Lamborghini', 'Ducati',
                        'Skania', 'Porsche', 'Bentley'):
            raise ValueError('"brand" не может, быть не Vag')
        self.brand = brand.capitalize()

    def init_age(self, age: int):
        """
        Инициализация атрибута age
        :param age: возраст автомобиля
        :return:  возраст автомобиля
        """
        if not isinstance(age, int):
            raise TypeError('"age" может быть только целым числом (int)')
        if not age >= 0:
            raise ValueError('"age" не может быть отрицательным')
        self.age = age

    def init_car_milage(self, car_milage: int):
        """
        Инициализация атрибута car_milage
        :param car_milage: пробег автомобиля
        :return: пробег автомобиля
        """
        if not isinstance(car_milage, int):
            raise TypeError('"car_milage" должен быть типа "int"')
        self.car_milage = car_milage

    def init_condition(self, condition: str):
        """
        Инициализация атрибута condition
        :param condition: состояние автомобиля
        :return: тип состояние автомобиля
        """
        if not isinstance(condition, str):
            raise TypeError('"condition" должен быть типа "str"')
        self.condition = condition

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()