import requests
from utils.api import Google_maps_api


"""Создание, изменение и удаление новой локации"""

class Test_create_location():

    def test_create_location(self):

        print()  # Вывод пустой строки для более наглядного результата теста

        print('\nМетод POST')
        result_post = Google_maps_api.create_location()
        place_id = result_post.json().get('place_id')

        print('\nМетод GET (проверка POST)')
        result_get = Google_maps_api.get_location(place_id)

        print('\nМетод PUT')
        result_put = Google_maps_api.update_location(place_id)

        print('\nМетод GET (проверка PUT)')
        result_get = Google_maps_api.get_location(place_id)

        print()