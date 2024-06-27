import random
import datetime
from data import NAMES, SURNAMES, STREETS, PERIODS


class RandomOrderData:

    @staticmethod
    def random_name():
        name = random.choice(NAMES)
        return name

    @staticmethod
    def random_surname():
        surname = random.choice(SURNAMES)
        return surname

    @staticmethod
    def random_address():
        address = f'{random.choice(STREETS)}, {random.randint(1,100)}'
        return address

    @staticmethod
    def random_phone_number(length=9):
        """
        Генерирует номер телефона фомата "79<заданное случайное количество символов>"
        :param length: длина номера телефона
        :return: случайный номер телефона
        """
        n = 1
        number = ''
        while n <= length:
            number += random.choice('1234567890')
            n += 1
        return f'79{number}'

    @staticmethod
    def order_date():
        """
        :return: Возвращает текущую дату в формате "DD.MM.YYYY"
        """
        now = datetime.datetime.now()
        return f'{now.day}.{now.month}.{now.year}'

    @staticmethod
    def random_period():
        return random.choice(PERIODS)

