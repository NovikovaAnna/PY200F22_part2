from typing import Union


def name_setter(args):
    pass


def author_setter(args):
    pass


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None
        self.name = name
        self.author = author



    @property
    def author(self) -> str:
        return self._author

    @author_setter
    def author(self, author: str):
        if isinstance(author, str):
            self._author = author
            return
        raise TypeError("Имя автора только str тип")

    @property
    def name(self)->str:
        return self._name

    @name_setter
    def name(self, name: str):
        if isinstance(name, str):
            self._name = name
            return
        raise TypeError("Название только str тип")



    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


def pages_setter(args):
    pass


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга  {self.name}. Автор {self.author}"

    @property
    def pages(self):
        return self._pages

    @pages_setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц только целое и положительное число ")
        if value >= 1:
            self._pages = value


def duration_setter(args):
    pass


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    @property
    def duration(self)-> float:
        return self._duration

    @duration_setter
    def duration(self,value:[int,float]):
        if not isinstance(value, (int,float)):
            raise ValueError("Продолжительность может быть только положительной")
        if value > 0:
            self._duration = float(value)

if __name__ == "__main__":
    a = PaperBook("Crime and Punishment","F.Dostoyevsky", 486)
    b = AudioBook("Viy", "N.Gogol", 2.45)


