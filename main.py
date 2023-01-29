class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})'


class AudioBook(Book):
    """Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = duration

    def __str__(self):
        return f"Аудио книга {self._name}. Автор {self._author}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})'


Book1 = PaperBook("Мастер и Маргарита", "М.А.Булгаков", 200)
print(Book1)
print(repr(Book1))
Book2 = AudioBook("Меч Предназначения", "А.Сапковский", 12.18)
print(Book2)
print(repr(Book2))
