import time
import requests

# Цикл проверки и авторизации сети
while True:
    # Проверка подключения к сети
    try:
        r = requests.get('http://172.30.0.36:8000/')
    except:
        print('Подключитесь к сети')
        time.sleep(120)
        continue
    # Проверка авторизации в сети
    try:
        auto = requests.get('https://www.google.ru/?hl=ru')
        if auto.status_code == requests.codes.ok:
            print('Вы авторизированы !')
    # Авторизация в сети
    except:
        print('Отправка POST-запроса')
        data = {
        'user': 'Guest',
        'password': ''
        }
        requests.post('http://172.30.0.36:8000/api/captiveportal/access/logon/0/', data=data)