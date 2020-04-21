from pprint import pprint
from urllib.parse import urlencode
import requests
import json

class User:

    def __init__(self, user_id, user_first_name, user_last_name):
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_url = f'https://vk.com/id{self.user_id}'


    def __str__(self):
        return self.user_url


def mutual_friends(token, user1_id, user2_id):
    response = requests.get(
        'https://api.vk.com/method/friends.getMutual',
        params={
            'access_token': token,
            'source_uid': user1_id,
            'target_uid': user2_id,
            'fields': 'city',
            'v': 5.103
        }
    )
    temp_dict = response.json()
    ids = ''
    for new_id in temp_dict['response']:
        ids = ids + ', ' + str(new_id)
    user_response = requests.get(
        'https://api.vk.com/method/users.get',
        params={
            'access_token': TOKEN,
            'user_ids': ids,
            'v': 5.103
        }
    )
    mutual_friends_list = []
    for friends in user_response.json()['response']:
        mutual_friends_list.append(User(friends['id'], friends['first_name'], friends['last_name']))
    return mutual_friends_list

APP_ID = 7412577
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status,friends',
    'response_type': 'token',
    'v': 5.52
}
#print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

#здесь использовались персональные данные
TOKEN = '48701da4a519b46259657292fb98d809059e42b446e0f3894023138a9ba13e1c4d36b132ee9c32e23754e'
user1 = User(4243253, 'EL', 'AL')
user2 = User(23289398, 'AN', 'SE')

# строка ниже использовалась для проверки работоспособности кода
print(mutual_friends(TOKEN, user1.user_id, user2.user_id)[0])






