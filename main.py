import json
import requests
from creat_settings import creat_settings_file
from pprint import pprint
from settings import TOKEN
from settings import name_dir
from settings import counts
from vk_access_token import access_token
from settings import user_id
from tqdm import tqdm


class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        uri = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(uri, params={**self.params, **params})
        return response.json()

    def photos_get(self, counts):
        uri = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'extended': 1, 'count': counts}
        response = requests.get(uri, params={**self.params, **params})
        return response.json()


class YA:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def create_folder(self, name):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/'
        requests.put(f'{uri}?path={name}', headers=self.get_headers())

    def upload_file(self, link, name):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        path = f"{name_dir}/{name}.jpg"
        params = {'url': link, 'path': path, 'disable_redirects': True}
        response = requests.post(uri, headers=self.get_headers(), params=params)
        return response


def grab_avatars(name_dir, res):
    if list(res.keys())[0] == 'error':
        return print('Страница удалена либо ещё не создана.')
    elif list(res.keys())[0] == 'response':
        if res['response']['count'] == 0:
            return print('На странице нет фото для загрузки.')
        elif res['response']['count'] > 0:
            for x in res.values():
                for y in x['items']:
                    if y['likes']['count'] in avatar_links.keys():
                        avatar_links.update({y['likes']['count'] + y['date']: y['sizes'][-1]})
                    else:
                        avatar_links.update({y['likes']['count']: y['sizes'][-1]})
    ya.create_folder(name_dir)
    for k, v in tqdm(avatar_links.items(), ncols=80, ascii=True, desc='Total'):
        ya.upload_file(v['url'], k)
    print(f'Uploaded, {counts} file(s) to a folder "{name_dir}"')
    for k, v in avatar_links.items():
        temp_dict = {}
        temp_dict['file_name'] = f'{k}.jpg'
        temp_dict['size'] = v['type']
        uploaded_files.append(temp_dict)
    return pprint(uploaded_files)


ya = YA(TOKEN)
vk = VK(access_token, user_id)
name_dir = name_dir
access_token = access_token
user_id = user_id
counts = counts
avatar_links = {}
uploaded_files = []

grab_avatars(name_dir, vk.photos_get(counts))

with open("upload_files.json", "w") as x:
    json.dump(uploaded_files, x)















