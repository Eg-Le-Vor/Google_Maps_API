import requests
from utils.api import Google_maps_api
from utils.checking import Checking


"""Создание, изменение и удаление новой локации"""

class Test_create_location():

    def test_create_location(self):

        print()  # Вывод пустой строки для более наглядного результата теста

        print('\nМетод POST')
        result_post = Google_maps_api.create_location()
        Checking.status_code(result_post, 200)
        place_id = result_post.json().get('place_id')

        print('\nМетод GET (проверка POST)')
        result_get_post = Google_maps_api.get_location(place_id)
        Checking.status_code(result_get_post, 200)

        print('\nМетод PUT')
        result_put = Google_maps_api.update_location(place_id)
        Checking.status_code(result_put, 200)

        print('\nМетод GET (проверка PUT)')
        result_get_put = Google_maps_api.get_location(place_id)
        Checking.status_code(result_get_put, 200)

        print('\nМетод DELETE')
        result_delete = Google_maps_api.delete_location(place_id)
        Checking.status_code(result_delete, 200)

        print('\nМетод GET (проверка DELETE)')
        result_get_delete = Google_maps_api.get_location(place_id)
        Checking.status_code(result_get_delete, 404)

        print()