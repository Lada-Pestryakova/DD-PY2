class FirstAidKit:
    def __init__(self, name: str, type_: str):
        """
        Базовый класс аптечка.

        :param name: Название препарата в аптечке
        :param type_: Тип препарата в аптечке
        """
        if not isinstance(name, str):
            raise TypeError("Название препарата должно быть типа str")
        self._name = name

        if not isinstance(type_, str):
            raise TypeError("Тип препарата должен быть типа str")
        if type_ not in ['таблетки', 'капли', 'спрей', 'сироп']:
            raise ValueError("Недоступный тип препарата")
        self._type = type_

    @property
    def name(self) -> str:
        """
        Инкапсулируем атрибут во избежание изменения установленных параметров существующих упаковок препаратов
        """
        return self._name

    @property
    def type_(self) -> str:
        """
        Инкапсулируем атрибут во избежание изменения установленных параметров существующих упаковок препаратов
        """
        return self._type

    def __str__(self) -> str:
        return f"Средство в аптечке - {self._name}. Тип средства - {self._type}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, type={self._type!r})"

    def how_much(self, drug) -> int:
        """
        Функция проверки наполненности препарата в аптечке

        :param drug: Название препарата для проверки
        :return:  Сколько препарата осталось в аптечке
        """
        ...

    def check_the_expiration_date(self, drug: str) -> bool:
        """
        Функция проверки срока годности препарата в аптечке

        :param drug: Название препарата для проверки
        :return: Годен ли препарат в аптечке
        """
        ...


class Antiviral(FirstAidKit):
    def __init__(self, name: str, type_: str, quantity: int):
        """
        Дочерний класс противовирусный препарат.

        :param name: Название препарата
        :param type_: Тип препарата
        :param quantity: Количество (в штуках таблеток)
        """
        super().__init__(name, type_)
        if not isinstance(quantity, int):
            raise TypeError("Количество таблеток должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество таблеток должно быть положительным числом")
        self.quantity = quantity

    @property
    def quantity(self) -> int:
        """
        Инкапсулируем атрибут во избежание изменения установленных параметров существующих упаковок препаратов
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        """
        Функция для изменения атрибута для отслеживания его актуального количества

        :param quantity: Новое количество препарата
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество таблеток должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество таблеток должно быть положительным числом")
        self._quantity = quantity

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self._name!r}, type={self._type!r}, quantity={self.quantity!r})'

    def how_much(self, drug) -> int:
        """
        Функция проверки наполненности выдает в результате количество препарата в аптечке,
        что заменяется на метод getter
        """
        ...


class Nasal(FirstAidKit):
    def __init__(self, name: str, type_: str, volume: int):
        """
        Дочерний класс назальное средство (против насморка).

        :param name: Название препарата
        :param type_: Тип препарата
        :param volume: Объем бутылька препарата (в мл)
        """
        super().__init__(name, type_)
        if not isinstance(volume, int):
            raise TypeError("Объем бутылька должен быть типа int")
        if volume <= 0:
            raise ValueError("Объем бутылька должен быть положительным числом")
        self.volume = volume

    @property
    def volume(self) -> int:
        """
        Инкапсулируем атрибут во избежание изменения установленных параметров существующих упаковок препаратов
        """
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        """
        Функция для изменения атрибута для отслеживания его актуального количества

        :param volume: Новое количество препарата
        """
        if not isinstance(volume, int):
            raise TypeError("Объем бутылька должен быть типа int")
        if volume <= 0:
            raise ValueError("Объем бутылька должен быть положительным числом")
        self._volume = volume

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self._name!r}, type={self._type!r}, volume={self.volume!r})'

    def how_much(self, drug) -> int:
        """
        Функция проверки наполненности выдает в результате количество препарата в аптечке,
        что заменяется на метод getter
        """
        ...


Drug1 = Antiviral("Стрепсилс", "таблетки", 24)
print(Drug1)
print(repr(Drug1))
Drug2 = Nasal("АкваМарис", "спрей", 30)
print(Drug2)
print(repr(Drug2))
