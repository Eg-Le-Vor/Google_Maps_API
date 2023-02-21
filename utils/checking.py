import json


"""Методы для проверки ответов запросов"""

class Checking:


    """Метод для проверки статус кода запроса"""

    @staticmethod
    def check_status_code(result, code):
        print(f'Статус код {result.status_code}. ', end='')
        assert code == result.status_code


    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(result, expected_value):
        assert list(json.loads(result.text)) == expected_value
        print('Все поля присутствуют.')