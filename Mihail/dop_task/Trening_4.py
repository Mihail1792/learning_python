import requests
import datetime

api_id = '6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru'


def current_weather(q):
    return requests.get(api_id + "weather", params=locals()).json()


if __name__ == "__main__":
    while True:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Minsk'
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
                                f'USD?parammode=2')
        if response.status_code == 200:
            json_data = response.json()
            cur_name = json_data.get("Cur_Name")
            off_rate = json_data.get("Cur_OfficialRate")
            print(f'Официальный курс {cur_name}: {off_rate}')
            break
        else:
            print("Код валюты введён неверно! Попробуйте снова.")




























# import requests
#
# url = 'https://www.youtube.com/results'
# query = {'search_query': 'python'}
# response = requests.get(url, params=query)
# print(response.url, 'url')


# c5d6386c
# response = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=K4Gin7W0SgEc58uUwUT1xItd0sgLs9L4pbGBuDpI')


# def func(one=1):
#     two = 2
#     tri = 3
#     f = 5
#     print(locals())
#
# func()


# import requests
# from pprint import pprint
# api_address = "http://api.openweathermap.org/data/2.5/weather?appid=6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru&q="
# while True:
#         city = input("Введите Ваш город: ")
#         url = api_address + city
#         json_data = requests.get(url).json()
#         my_format = {}
#         response = requests.get(url) #Переменная с данными запрса реквест
#         if response.status_code == 200:
#             city = json_data.get('name')
#             temp_max = json_data.get('main')
#             for i in temp_max:
#                 my_format.update({i: temp_max.get(i)})
#             print(f'{pprint(my_format)}{city}')
#             print((requests.get(api_address + city)).status_code)
#         else:
#             print("Данные введёны некорректно!")

# import requests
# URL_BASE = "http://api.openweathermap.org/data/2.5/"
# APPID = "6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru"
# response = requests.get
# def pogoda(city, appid):
#     return requests.get(URL_BASE + "weather", params=locals()).json()
#
# if __name__ == "__main__":
#     from pprint import pprint
#     while True:
#         city = input(":")
#         print(pogoda(city))


# import requests
#
# APPID = "6c66a53d3dc8634021977ec4de5be7a5"
# URL_BASE = "http://api.openweathermap.org/data/2.5/"
#
#
# def current_weather(q: str = "Minsk", appid: str = APPID) -> dict:
#     # """https://openweathermap.org/api"""
#     return requests.get(URL_BASE + "weather", params=locals()).json()
#
# if __name__ == "__main__":
#     from pprint import pprint
#
#     while True:
#         location = input("Enter a location:").strip()
#         if location:
#             pprint(current_weather(location))
#         else:
#             break


# zapros = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city("Введите Ваш город: ")}&appid=6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru')
# return zapros


# def weather_forecast(q: str = "Kolkata, India", appid: str = APPID) -> dict:
#     """https://openweathermap.org/forecast5"""
#     return requests.get(URL_BASE + "forecast", params=locals()).json()
#
#
# def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
#     """https://openweathermap.org/api/one-call-api"""
#     return requests.get(URL_BASE + "onecall", params=locals()).json()

# weather?id=524901&lang=ru


# import requests
# from pprint import pprint
# import datetime
#
# response = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=K4Gin7W0SgEc58uUwUT1xItd0sgLs9L4pbGBuDpI')
# json_data = response.json()
# pprint(json_data)


# https://api.nasa.gov/planetary/apod?api_key=K4Gin7W0SgEc58uUwUT1xItd0sgLs9L4pbGBuDpI


# number_list = [7, 4, 9]
# number_list.insert(1, ("4 - 2"))
# f = [int(item) for item in number_list]
# print(f)
# a = sum(number_list)
# print(number_list.index(4))

# print(number_list)
# number_list.append((4-2))
# number_list.remove(7)


# my_number_list = []
# for i in number_list:
#     number_list.append(i - 2)
#
# # number_list.append(1)
# print(number_list)


# import requests
# import datetime
#
# api_id = '6c66a53d3dc8634021977ec4de5be7a5&units=metric&lang=ru'
#
#
# def current_weather(q):
#     return requests.get(api_id + "weather", params=locals()).json()
#
#
# if __name__ == "__main__":
#     while True:
#         response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input("Введите Ваш город: ")}'
#                                 f'&appid={api_id}')
#         json_data = response.json()
#         if response.status_code == 200:
#             max_temp = json_data["main"]["temp_max"]
#             city = json_data["name"]
#             cur_weather = json_data["main"]["temp"]
#             humidity = json_data["main"]["humidity"]
#             pressure = json_data["main"]["pressure"]
#             wind = json_data["wind"]["speed"]
#             sunrise = datetime.datetime.fromtimestamp(json_data["sys"]["sunrise"])
#             print(f'Погода в городе: {city}\nТемпература воздуха: {(cur_weather) // 1}°C\n'
#                   f'Влажность: {humidity}%\nАтмосферное давление: {((pressure) / 1.333) // 1}мм.рт.ст.\n'
#                   f'Скорость ветра: {wind}м/c\nВремя восхода солнца: {sunrise}\n'
#                   f'Максимальная температура: {max_temp}°C'
#                   )
#             break
#         else:
#             print("Город введён некорректно!")
#
#
# URL_BASE = "https://www.nbrb.by/api/exrates/rates/"
#
#
# def cur_rate(q):
#     return requests.get(URL_BASE, params=locals()).json()
#
#
# if __name__ == "__main__":
#     while True:
#         response = requests.get(f'{URL_BASE}'
#                                 f'{input("Введите код валюты (USD, EUR, RUB): ")}?parammode=2')
#         if response.status_code == 200:
#             json_data = response.json()
#             cur_name = json_data.get("Cur_Name")
#             off_rate = json_data.get("Cur_OfficialRate")
#             print(f'Официальный курс {cur_name}: {off_rate}')
#             break
#         else:
#             print("Код валюты введён неверно! Попробуйте снова.")
