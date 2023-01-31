from utils.http_methods import HttpMethods
"""GMaps api testing methods"""

base_url = 'https://rahulshettyacademy.com'  # base URL
key = '?key=qaclick123'               # Параметр для всех запросов


class GoogleMapsApi:

    """method for creating a new location"""
    @staticmethod
    def create_new_place():

        json_for_creating_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        post_resourse = '/maps/api/place/add/json'    # Ресурс метода Post
        post_url = base_url + post_resourse + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_creating_new_place)
        print(result_post.text)
        return result_post

    """method for checking the creation of a new location"""
    @staticmethod
    def check_create_new_place(place_id):

        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """method for updating the location"""
    @staticmethod
    def update_the_place(place_id):

        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Baker street, London",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_location)
        print(result_put.text)
        return result_put

    """method for deleting the location"""
    @staticmethod
    def delete_the_place(place_id):

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id,
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete
