import requests
import datetime

api_id = '6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru'


def current_weather(q):
    return requests.get(api_id + "weather", params=locals()).json()


if __name__ == "__main__":
    while True:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input("Введите Ваш город: ")}'
                                f'&appid={api_id}')
        json_data = response.json()
        if response.status_code == 200:
            max_temp = json_data["main"]["temp_max"]
            city = json_data["name"]
            cur_weather = json_data["main"]["temp"]
            humidity = json_data["main"]["humidity"]
            pressure = json_data["main"]["pressure"]
            wind = json_data["wind"]["speed"]
            sunrise = datetime.datetime.fromtimestamp(json_data["sys"]["sunrise"])
            print(f'Погода в городе: {city}\nТемпература воздуха: {(cur_weather) // 1}°C\n'
                  f'Влажность: {humidity}%\nАтмосферное давление: {((pressure) / 1.333) // 1}мм.рт.ст.\n'
                  f'Скорость ветра: {wind}м/c\nВремя восхода солнца: {sunrise}\n'
                  f'Максимальная температура: {max_temp}°C'
                  )
            break
        else:
            print("Город введён некорректно!")


URL_BASE = "https://www.nbrb.by/api/exrates/rates/"


def cur_rate(q):
    return requests.get(URL_BASE, params=locals()).json()


if __name__ == "__main__":
    while True:
        response = requests.get(f'{URL_BASE}'
                                f'{input("Введите код валюты (USD, EUR, RUB): ")}?parammode=2')
        if response.status_code == 200:
            json_data = response.json()
            cur_name = json_data.get("Cur_Name")
            off_rate = json_data.get("Cur_OfficialRate")
            print(f'Официальный курс {cur_name}: {off_rate}')
            break
        else:
            print("Код валюты введён неверно! Попробуйте снова.")

