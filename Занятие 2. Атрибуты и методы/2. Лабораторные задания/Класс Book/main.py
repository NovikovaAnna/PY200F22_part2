BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:


    def __init__(self, id_: int, name: str, pages: int):
        """
        Подготовка  и инициализация
        :param id_:  номер книги
        :param name: название книги
        :param pages: количество страниц
        """
        self.id_ = None
        self.name = None
        self.pages = None
        self.init_id(id_)
        self.init_name(name)
        self.init_pages(pages)

    def init_id(self, id_: int):
        """
        Инициализация атрибута id_
        :param id_: номер книги
        """
        if not isinstance(id_, int):
            raise TypeError("ID должен быть целым числом")
        if id_ <= 0:
            raise ValueError("ID должен быть больше нуля")
            self.id_ = id_

    def init_name(self, name):
        """
        Инициализация атрибута name
        :param name: название книги
        """
        if not isinstance(name, str):
            raise TypeError("Название книги только типа str")
            self.name = name

    def init_pages(self, pages):
        """
        Инициализация атрибута pages
        :param pages: количество страниц
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц может быть тольок целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
            self.pages = pages

    def __str__(self):
    """
    Строковое предстваление объекта
    :return: Строковое предстваление объекта
    """
        return f'Книга "{self.name}"'

    def __repr__(self):
    """
    Метод repr для класса Book
    :return: Возвращает название класса со всеми значениями его атрибутов
    """
        return f"{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"



if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
    print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
