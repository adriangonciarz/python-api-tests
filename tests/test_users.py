import requests
from config import endpoints


class TestUsers:
    """Users Tests: """

    def test_create_new_user(self, user):
        """Create new user and validate it can be found via resource"""
        user_body, user_id = user
        fetched_user = requests.get(endpoints.user_with_id(user_id)).json()
        expected = user_body.copy()
        expected['id'] = user_id

        assert fetched_user == expected
