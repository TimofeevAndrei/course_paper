def creat_settings_file():
    TOKEN = input('Введите токен Яндекс.Полигона: ')
    user_id = input('Введите VK User_id: ')
    counts = input('Сколько фото загрузить: ')
    f = open("settings.py", "w")
    f.write(f'TOKEN = "{TOKEN}" \n')
    f.write(f'user_id = "{user_id}" \n')
    f.write(f'counts = "{counts}" \n')
    f.close()


creat_settings_file()