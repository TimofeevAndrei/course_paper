def creat_settings_file():
    TOKEN = input('Введите токен Яндекс.Полигона: ')
    access_token = input('Введите токен VK: ')
    user_id = input('Введите VK User_id: ')
    f = open("settings.py", "w")
    f.write(f'TOKEN = "{TOKEN}" \n')
    f.write(f'access_token = "{access_token}" \n')
    f.write(f'user_id = "{user_id}" \n')
    f.close()


creat_settings_file()

import json
import requests
from pprint import pprint
from settings import TOKEN
from settings import access_token
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

   def photos_get(self):
       uri = 'https://api.vk.com/method/photos.get'
       params = {'user_ids': self.id, 'album_id': 'profile', 'extended': 1}
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

    # Вопрос хотел использовать данный метод для формирования основы для json файла по итогу загрузки
    # но сколько не старался, данный метод пропускал один последний загружаемый файл. Так и не поняли в чем проблема
    # def file_info(self, num):
    #     uri = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'
    #     params = {'limit': num, 'fields': 'items.name'}
    #     response = requests.get(uri, headers=self.get_headers(), params=params)
    #     return response.json()


def grab_avatars(size):
    for x in res.values():
        for y in x['items']:
            for s in y['sizes']:
                if s['type'] == size:
                    if y['likes']['count'] in avatar_links.keys():
                        avatar_links.update({y['likes']['count'] + y['date']: s['url']})
                    else:
                        avatar_links.update({y['likes']['count']: s['url']})
    ya.create_folder(name_dir)
    num = 0
    for k, v in tqdm(avatar_links.items(), ncols=80, ascii=True, desc='Total'):
        num += 1
        if num == 11:
            break
        ya.upload_file(v, k)
    print(f'Uploaded, {num} file(s) to a folder "{name_dir}"')
    if len(avatar_links) == num:
        for k in avatar_links.keys():
            temp_dict = {}
            temp_dict['file_name'] = f'{k}.jpg'
            temp_dict['size'] = size
            uploaded_files.append(temp_dict)
    return pprint(uploaded_files)


size = 'z'
name_dir = 'avatar'
ya = YA(TOKEN)
access_token = access_token
user_id = user_id
vk = VK(access_token, user_id)
res = vk.photos_get()
avatar_links = {}
uploaded_files = []

grab_avatars(size)

with open("upload_files.json", "w") as x:
    json.dump(uploaded_files, x)

# Осталось сделать ввод токенов и айди
# Все зависимости должны быть указаны в файле requiremеnts.txt













