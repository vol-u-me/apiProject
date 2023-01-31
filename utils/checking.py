
"""methods for checking responses to requests"""
from requests import Response


class Cheking:
    """Status code check"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        print('Successfully! Status code is: ', response.status_code)