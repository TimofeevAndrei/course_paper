import json
import requests
from settings import TOKEN
from pprint import pprint
from settings import access_token
from settings import user_id

class VK:
   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()

   def photos_get(self):
       self.aid = 'profile'
       url = 'https://api.vk.com/method/photos.get'
       params = {'user_ids': self.id, 'album_id': self.aid, 'extended': 1}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = access_token
user_id = user_id
vk = VK(access_token, user_id)
res = vk.photos_get()
# pprint(res)
avatar_links = {}
for x in res.values():
    for y in x['items']:
        # pprint(y)
        for s in y['sizes']:
            if s['type'] == 'z':
                if y['likes']['count'] in avatar_links.keys():
                    avatar_links.update({y['likes']['count'] + y['date']: s['url']})
                else:
                    avatar_links.update({y['likes']['count']: s['url']})



pprint(avatar_links)








