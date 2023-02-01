import allure
from utils.api import GoogleMapsApi
from utils.checking import Cheking


"""Create, edit and del new location"""


@allure.epic('Test create place')
class TestCreatePlace:
    result_post = GoogleMapsApi.create_new_place()
    place_id = GoogleMapsApi.create_new_place().json().get("place_id")

    @allure.description('Test create new location')
    def test_create_new_place(self, place_id=place_id, result_post=result_post):
        print()
        print('POST method')
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print()
        print('GET method for check creation')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        print('___________________________________________________')
        print('Create new location testing completed')

    @allure.description('Test edit location')
    def test_update(self, place_id=place_id):
        print()
        print('PUT method')
        result_put = GoogleMapsApi.update_the_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print()
        print('GET method for check update')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', '100 Baker street, London')
        print('___________________________________________________')
        print('Edit location testing completed')

    @allure.description('Test delete new location')
    def test_delete(self, place_id=place_id):
        print()
        print('DELETE method')
        result_delete = GoogleMapsApi.delete_the_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print()
        print('GET method for check deleting')
        result_get = GoogleMapsApi.check_create_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        Cheking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print('___________________________________________________')
        print('Delete new location testing completed')
