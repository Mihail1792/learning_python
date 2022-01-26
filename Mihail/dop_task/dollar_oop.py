import requests


class ExchangeRates:
    URL_BASE = "https://www.nbrb.by/api/exrates/rates/"

    def cur_rate(self):
        return requests.get(self.URL_BASE, params=locals()).json()

    while True:
        response = requests.get(f'{URL_BASE}USD?parammode=2')
        if response.status_code == 200:
            json_data = response.json()
            cur_name = json_data.get("Cur_Name")
            off_rate = json_data.get("Cur_OfficialRate")
            print(f'Официальный курс {cur_name}: {off_rate}')
            break
        else:
            print("Код валюты введён неверно! Попробуйте снова.")







# URL_BASE = "https://www.nbrb.by/api/exrates/rates/"
# def cur_rate(q):
#     return requests.get(URL_BASE, params=locals()).json()
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
