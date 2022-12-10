from typing import Union
import doctest  # TODO Написать 3 класса с документацией и аннотацией типов


class BallOfYarn:
    def __init__(self, weight: Union[int, float], length: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Клубок ниток"

        :param weight: Вес нити в клубке (в граммах)
        :param length: Длина нити в клубке (в метрах)
        :param color: Цвет нити

        Пример:
        >>> red_yarn = BallOfYarn(300, 250, 'red') #инициализация экземпляра класса
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес нити должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес нити должен быть положительным числом")
        self.weight = weight

        if not isinstance(length, (int, float)):
            raise TypeError("Длина нити должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина нити должна быть положительным числом")
        self.length = length

        if not isinstance(color, str):
            raise TypeError("Цвет нити должен быть типа str")
        if color not in ['red', 'blue', 'green', 'yellow']:
            raise ValueError("Недоступный цвет нити")
        self.color = color

    def knit_a_scarf(self, weight_of_scarf: Union[int, float]) -> None:
        """
        Вяжем спицами шарф - расходуем нить

        :param weight_of_scarf: Вес желаемого шарфа
        :raise ValueError: Если вес шарфа превосходит вес клубка нити, то возвращается ошибка

        Пример:
        >>> red_yarn = BallOfYarn(300, 250, 'red')
        >>> red_yarn.knit_a_scarf(250)
        """
        if not isinstance(weight_of_scarf, (int, float)):
            raise TypeError("Вес шарфа должен быть типа int или float")
        if weight_of_scarf <= 0:
            raise ValueError("Вес шарфа должен быть положительным числом")
        ...

    def crochet_a_hat(self, weight_of_hat: Union[int, float]) -> None:
        """
        Вяжем крючком шапку - расходуем нить

        :param weight_of_hat: Вес желаемой шапки
        :raise ValueError: Если вес шапки превосходит вес клубка, то возвращается ошибка

        Пример:
        >>> green_yarn = BallOfYarn(400, 200, 'green')
        >>> green_yarn.crochet_a_hat(303.5)
        """
        if not isinstance(weight_of_hat, (int, float)):
            raise TypeError("Вес шапки должен быть типа int или float")
        if weight_of_hat <= 0:
            raise ValueError("Вес шапки должен быть положительным числом")
        ...


class BoxOfCandies:
    def __init__(self, number_of_candies: int, box_capacity: int):
        """
        Создание и подготовка к работе объекта "Коробка конфет"

        :param number_of_candies: Количество конфет в коробке (в шт. конфет)
        :param box_capacity: Вместимость коробки (в шт. конфет)

        Пример:
        >>> full_box = BoxOfCandies(12,12)
        """
        if not isinstance(number_of_candies, int):
            raise TypeError("Количество конфет должно быть типа int")
        if number_of_candies < 0:
            raise ValueError("Количество конфет не должно быть отрицательным числом")
        self.number_of_candies = number_of_candies

        if not isinstance(box_capacity, int):
            raise TypeError("Вместимость коробки должна быть типа int")
        if box_capacity <= 0:
            raise ValueError("Вместимость коробки должна быть положительным числом")
        self.box_capacity = box_capacity

    def is_full_box(self) -> bool:
        """
        Функция проверки наполненности коробки конфет

        :return: Является ли коробка полной

        Пример:
        >>> box1 = BoxOfCandies(3, 12)
        >>> box1.is_full_box()
        """
        ...

    def take_candies(self, candies: int) -> int:
        """
        Берем конфеты из коробки

        :param candies: Количество конфет, которое хотим взять из коробки
        :raise ValueError: Если конфет в коробке не хватает, возвращается ошибка
        :return: Остаток конфет в коробке

        Пример:
        >>> box2 = BoxOfCandies(5, 10)
        >>> box2.take_candies(3)
        """
        if not isinstance(candies, int):
            raise TypeError("Количество конфет должно быть типа int")
        if candies <= 0:
            raise ValueError("Количество конфет должно быть положительным числом")
        ...

    def put_candies(self, candies: int) -> int:
        """
        Кладем конфеты в коробку

        :param candies: Количество конфет, которое хотим положить в коробку
        :raise ValueError: Если количество конфет превышает вместимость коробки, возвращается ошибка
        :return: Новое количество конфет в коробке

        Пример:
        >>> box3 = BoxOfCandies(7, 12)
        >>> box3.put_candies(3)
        """
        if not isinstance(candies, int):
            raise TypeError("Количество конфет должно быть типа int")
        if candies <= 0:
            raise ValueError("Количество конфет должно быть положительным числом")
        ...


class Password:
    def __init__(self, length: int, security: str):
        """
        Создание и подготовка к работе объекта "Пароль"

        :param length: Длина пароля
        :param security: Надежность пароля (его сложность)

        Пример:
        >>> password1 = Password(8, 'high')
        """
        if not isinstance(length, int):
            raise TypeError("Длина пароля должна быть типа int")
        if length <= 0:
            raise ValueError("Длина пароля должна быть положительным числом")
        self.length = length

        if not isinstance(security, str):
            raise TypeError("Надежность пароля должна быть типа str")
        if security not in ['low', 'average', 'high']:
            raise ValueError("Неверное обозначение надежности пароля")
        self.security = security

    def correct_password_for_mail(self, required_length: int, required_security: str) -> bool:
        """
        Установка пароля для электронной почты

        :param required_length: Требуемая длина пароля
        :param required_security: Требуемая надежность пароля
        :raise ValueError: Если длина пароля не соответствует требованиям, возвращается ошибка
        :raise ValueError: Если надежность пароля не соответствует требованиям, возвращается ошибка
        :return: Подходит ли пароль или нет

        Пример:
        >>> password2 = Password(8,'low')
        >>> password2.correct_password_for_mail(12,'high')
        """
        if not isinstance(required_length, int):
            raise TypeError("Требуемая длина пароля должна быть типа int")
        if required_length <= 0:
            raise ValueError("Требуемая лина пароля должна быть положительным числом")

        if not isinstance(required_security, str):
            raise TypeError("Требуемая надежность пароля должна быть типа str")
        if required_security not in ['low', 'average', 'high']:
            raise ValueError("Неверное обозначение требуемой надежности пароля")
        ...

    def change_password_for_mail(self, required_length: int, required_security: str) -> None:
        """
        Смена пароля для почты
        :param required_length: Требуемая длина пароля
        :param required_security: Требуемая надежность пароля
        :raise ValueError: Если длина пароля не соответствует требованиям, возвращается ошибка
        :raise ValueError: Если надежность пароля не соответствует требованиям, возвращается ошибка
        :raise ValueError: Если новый пароль совпадает со старым паролем, возвращается ошибка
        :return: Подходит пароль или нет
        """
        if not isinstance(required_length, int):
            raise TypeError("Требуемая длина пароля должна быть типа int")
        if required_length <= 0:
            raise ValueError("Требуемая лина пароля должна быть положительным числом")

        if not isinstance(required_security, str):
            raise TypeError("Требуемая надежность пароля должна быть типа str")
        if required_security not in ['low', 'average', 'high']:
            raise ValueError("Неверное обозначение требуемой надежности пароля")
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
