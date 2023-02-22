import datetime
import os


LOGS_PATH = "logs/log_"
LOGS_EXT = ".log"


"""Методы для логгирования"""

class Logger():


    """Создание файла логов"""

    file_name = LOGS_PATH + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + LOGS_EXT


    """Метод записи лога в файл"""

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)


    """Метод создания лога запроса"""

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"-----REQUEST------\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}"
        data_to_add += f"\n------------------\n"
        cls.write_log_to_file(data_to_add)


    """Метод создания лога ответа"""

    @classmethod
    def add_response(cls, result):
        headers_as_dict = dict(result.headers)
        cookies_as_dict = dict(result.cookies)
        data_to_add = f"-----RESPONSE-----\n"
        data_to_add += f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}"
        data_to_add += f"\n------------------\n\n"
        cls.write_log_to_file(data_to_add)