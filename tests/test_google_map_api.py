import os
import json
import allure
from utils.api import Google_maps_api
from utils.checking import Checking


DIR_PATH = os.path.dirname(os.path.realpath(__file__))  # Путь к директории
RESPONSE_CREATE_LOCATION_200_PATH = "files/response/create_location_200.json"  # Путь к JSON файлам, которые содержат RESPONSE запросов
RESPONSE_UPDATE_LOCATION_200_PATH = "files/response/update_location_200.json"
RESPONSE_DELETE_LOCATION_200_PATH = "files/response/delete_location_200.json"
RESPONSE_GET_LOCATION_200_PATH = "files/response/get_location_200.json"
RESPONSE_UPDATE_LOCATION_404_PATH = "files/response/update_location_404.json"
RESPONSE_DELETE_LOCATION_404_PATH = "files/response/delete_location_404.json"
RESPONSE_GET_LOCATION_404_PATH = "files/response/get_location_404.json"


"""Создание, изменение и удаление новой локации"""

@allure.epic("Test create place")
class Test_create_location():

    @allure.description("Test create, update, delete place")
    def test_create_location(self):

        print()  # Вывод пустой строки для более наглядного результата теста

        print('\nМетод POST')
        result_post = Google_maps_api.create_location()
        Checking.check_status_code(result_post, 200)
        with open(os.path.join(DIR_PATH, RESPONSE_CREATE_LOCATION_200_PATH), 'r') as create_f:
            temp = json.load(create_f)
            response_create_location_tokens = list(temp.keys())
        Checking.check_json_token(result_post, response_create_location_tokens)
        place_id = result_post.json().get('place_id')

        print('\nМетод GET (проверка POST)')
        result_get_post = Google_maps_api.get_location(place_id)
        Checking.check_status_code(result_get_post, 200)
        with open(os.path.join(DIR_PATH, RESPONSE_GET_LOCATION_200_PATH), 'r') as get_post_f:
            temp = json.load(get_post_f)
            response_get_post_location_tokens = list(temp.keys())
        Checking.check_json_token(result_get_post, response_get_post_location_tokens)

        print('\nМетод PUT')
        result_put = Google_maps_api.update_location(place_id)
        Checking.check_status_code(result_put, 200)
        with open(os.path.join(DIR_PATH, RESPONSE_UPDATE_LOCATION_200_PATH), 'r') as update_f:
            temp = json.load(update_f)
            response_update_location_tokens = list(temp.keys())
        Checking.check_json_token(result_put, response_update_location_tokens)

        print('\nМетод GET (проверка PUT)')
        result_get_put = Google_maps_api.get_location(place_id)
        Checking.check_status_code(result_get_put, 200)
        with open(os.path.join(DIR_PATH, RESPONSE_GET_LOCATION_200_PATH), 'r') as get_put_f:
            temp = json.load(get_put_f)
            response_get_put_location_tokens = list(temp.keys())
        Checking.check_json_token(result_get_put, response_get_put_location_tokens)

        print('\nМетод DELETE')
        result_delete = Google_maps_api.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        with open(os.path.join(DIR_PATH, RESPONSE_DELETE_LOCATION_200_PATH), 'r') as delete_f:
            temp = json.load(delete_f)
            response_delete_location_tokens = list(temp.keys())
        Checking.check_json_token(result_delete, response_delete_location_tokens)

        print('\nМетод GET (проверка DELETE)')
        result_get_delete = Google_maps_api.get_location(place_id)
        Checking.check_status_code(result_get_delete, 404)
        with open(os.path.join(DIR_PATH, RESPONSE_GET_LOCATION_404_PATH), 'r') as get_delete_f:
            temp = json.load(get_delete_f)
            response_get_delete_location_tokens = list(temp.keys())
        Checking.check_json_token(result_get_delete, response_get_delete_location_tokens)

        print()