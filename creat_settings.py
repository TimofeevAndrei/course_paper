def creat_settings_file():
    TOKEN = input('Введите токен Яндекс.Полигона: ')
    user_id = input('Введите VK User_id: ')
    counts = input('Сколько фото загрузить: ')
    name_dir = input('Введите название новой папки для файлов: ')
    f = open("settings.py", "w")
    f.write(f'TOKEN = "{TOKEN}" \n')
    f.write(f'user_id = "{user_id}" \n')
    f.write(f'counts = "{counts}" \n')
    f.write(f'name_dir = "{name_dir}" \n')
    f.close()


creat_settings_file()