from pprint import pprint
from urllib.parse import urlencode
import requests
import json

APP_ID = 7412577
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status,friends',
    'response_type': 'token',
    'v': 5.52
}

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = 'b9e91fda083b778cc96fedf9746bb74a77d2d0a25b755f4b2e1c912047f264bb900ac2322c85136b20069'

response = requests.get(
    'https://api.vk.com/method/friends.getMutual',
    params={
        'access_token': TOKEN,
        'target_uid': 4243253,
        'fields': 'city',
        'v': 5.103
    }
)
pprint(response.json())