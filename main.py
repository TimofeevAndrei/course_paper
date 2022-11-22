import json
import requests
from settings import TOKEN
from pprint import pprint
from settings import access_token
from settings import user_id
from tqdm import tqdm
from time import sleep



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


class YA:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def create_folder(self, name):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
        requests.put(f'{URL}?path={name}', headers=self.get_headers())

    def upload_file(self, link, name):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        path = f"{name_dir}/{name}"
        params = {'url': link, 'path': path, 'disable_redirects': True}
        response = requests.post(uri, headers=self.get_headers(), params=params)
        # pprint(response)




def grab_avatars():
    for x in res.values():
        for y in x['items']:
            # pprint(y)
            for s in y['sizes']:
                if s['type'] == 'z':
                    if y['likes']['count'] in avatar_links.keys():
                        avatar_links.update({y['likes']['count'] + y['date']: s['url']})
                    else:
                        avatar_links.update({y['likes']['count']: s['url']})
    ya.create_folder(name_dir)
    for k, v in tqdm(avatar_links.items(), ncols=80, ascii=True, desc='Total'):
        ya.upload_file(v, k)

    return print('Загрузка завершена')


name_dir = 'avatar'
ya = YA(TOKEN)
access_token = access_token
user_id = user_id
vk = VK(access_token, user_id)
res = vk.photos_get()
avatar_links = {}

grab_avatars()









