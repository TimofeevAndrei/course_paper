def creat_settings_file():
    TOKEN = input('Введите токен Яндекс.Полигона: ')
    user_id = input('Введите VK User_id: ')
    f = open("settings.py", "w")
    f.write(f'TOKEN = "{TOKEN}" \n')
    f.write(f'user_id = "{user_id}" \n')
    f.close()


creat_settings_file()