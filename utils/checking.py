import json
from requests import Response


"""methods for checking responses to requests"""
class Cheking:
    """Status code check"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        print('Successfully! Status code is: ', response.status_code)


    """method to check for required fields"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('all required fields are in JSON')


    """Method for checking the contents of fields"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name, 'is correct!')