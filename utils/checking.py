"""Методы для проверки ответов запросов"""

class Checking():


    """Метод для проверки статус кода запроса"""

    @staticmethod
    def status_code(result, code):
        print(f'Статус код {result.status_code}. ', end='')
        assert code == result.status_code
        print('Успешно.')