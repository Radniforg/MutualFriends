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
    for id in temp_dict['response']:
        ids = ids + ', ' + str(id)
    user_response = requests.get(
        'https://api.vk.com/method/users.get',
        params={
            'access_token': TOKEN,
            'user_ids': ids,
            'v': 5.103
        }
    )
    MutualFriendsList = []
    for friends in user_response.json()['response']:
        MutualFriendsList.append(User(friends['id'], friends['first_name'], friends['last_name']))
    return MutualFriendsList

user1 = User(6293784, 'Иван', 'Александров')
user2 = User(4243253, 'Елена,', 'Александрова')

APP_ID = 7412577
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status,friends',
    'response_type': 'token',
    'v': 5.52
}
TOKEN = 'b9e91fda083b778cc96fedf9746bb74a77d2d0a25b755f4b2e1c912047f264bb900ac2322c85136b20069'

print(mutual_friends(TOKEN, user1.user_id, user2.user_id)[0])






