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

    def __and__(self, other_user):
        response_first = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': TOKEN,
                'user_id': self.user_id,
                'v': 5.103
            }
        )
        response_second = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': other_user.user_id,
                'v': 5.103
            }
        )
        ids = ''
        for first_user_friend in response_first.json()['response']['items']:
            for second_user_friend in response_second.json()['response']['items']:
                if first_user_friend == second_user_friend:
                    ids = ids + ', ' + str(first_user_friend)
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
pprint(user1&user2)






