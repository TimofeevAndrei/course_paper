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
       params = {'user_ids': self.id, 'album_id': self.aid}
       response = requests.get(url, params={**self.params, **params})
       res = response.json()
       return res


access_token = access_token
user_id = user_id
vk = VK(access_token, user_id)
pprint(vk.photos_get())


