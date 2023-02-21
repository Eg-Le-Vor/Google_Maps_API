import json
import os
from utils.http_methods import Http_methods


BASE_URL = "https://rahulshettyacademy.com"  # Базовый URL
KEY = "?key=qaclick123"  # Параметр для всех запросов
DIR_PATH = os.path.dirname(os.path.realpath(__file__))  # Путь к директории
CREATE_LOCATION_PATH = "files/create_location.json"  # Путь к JSON файлам
UPDATE_LOCATION_PATH = "files/update_location.json"
DELETE_LOCATION_PATH = "files/delete_location.json"


resources = {"GET": "/maps/api/place/get/json",  
             "POST": "/maps/api/place/add/json",
             "PUT": "/maps/api/place/update/json",
             "DELETE": "/maps/api/place/delete/json"}  # Ресурсы для методов GET, POST, PUT, DELETE


"""Методы для тестирования Google Maps API"""

class Google_maps_api:


    """Метод для проверка статус-кода запроса"""

    @staticmethod
    def status_code(result):
        print(f'Статус код {result.status_code}. ', end='')
        try:
            assert 200 == result.status_code
            print('Успешно.')
        except AssertionError:
            print('Неуспешно.')


    """Метод для создания новой локации"""

    @staticmethod
    def create_location():
        with open(os.path.join(DIR_PATH, CREATE_LOCATION_PATH), 'r') as create_f:
            json_create_location = json.load(create_f)
        url = BASE_URL + resources["POST"] + KEY
        print(f'URL: {url}')
        result = Http_methods.post(url, json_create_location)
        Google_maps_api.status_code(result)
        print(f'Результат: {result.text}')
        return result
    

    """Метод для получения информации о локации"""

    @staticmethod
    def get_location(place_id):
        url = BASE_URL + resources["GET"] + KEY + "&place_id=" + place_id
        print(f'URL: {url}')
        result = Http_methods.get(url)
        Google_maps_api.status_code(result)
        print(f'Результат: {result.text}')
        return result
    

    """Метод для обновления информации о существующей локации"""

    @staticmethod
    def update_location(place_id):
        with open(os.path.join(DIR_PATH, UPDATE_LOCATION_PATH), 'r') as update_f:
            json_update_location = json.load(update_f)
            json_update_location["place_id"] = place_id
        url = BASE_URL + resources["PUT"] + KEY
        print(f'URL: {url}')
        result = Http_methods.put(url, json_update_location)
        Google_maps_api.status_code(result)
        print(f'Результат: {result.text}')
        return result