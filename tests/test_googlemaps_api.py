from utils.api import GoogleMapsApi
from utils.checking import Cheking
"""Create, edit and del new location"""


class TestCreatePlace:

    def test_create_new_place(self):
        print()
        print('POST method')
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, 200)
        print(result_post.status_code)


        print()
        print('GET method for check creation')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 200)

        print()
        print('PUT method')
        result_put = GoogleMapsApi.update_the_place(place_id)
        Cheking.check_status_code(result_put, 200)

        print()
        print('GET method for check update')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 200)

        print()
        print('DELETE method')
        result_delete = GoogleMapsApi.delete_the_place(place_id)
        Cheking.check_status_code(result_delete, 200)

        print()
        print('GET method for check deleting')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 404)