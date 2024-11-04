import logging
import unittest
import os  # Импортируем модуль os для работы с файловой системой

# Проверка и удаление файла логов, если он существует
log_file = 'runner_tests.log'

if os.path.exists(log_file):
    os.remove(log_file)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')

        self.distance = 0

        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            Runner('Тест', -5)  # Исправлено на строку
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)  # Логируем с сообщением об ошибке


    def test_run(self):
        try:
            Runner(123, 10)  # Исправлено на число, но должно быть строкой
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)  # Логируем с сообщением об ошибке


if __name__ == '__main__':
    unittest.main()