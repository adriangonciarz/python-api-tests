from config.config import API_URL

USERS = f'{API_URL}/users'


def user_with_id(user_id):
    return f'{USERS}/{user_id}'
