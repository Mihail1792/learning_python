# import json
# from pprint import pprint
# import requests
# from bs4 import BeautifulSoup
#
# JSON = 'market.json'
# HOST = 'https://www.mebelshara.ru/'
# URL = 'https://www.mebelshara.ru/contacts/'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
# }
#
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='city-item')
#     markets = []
#     # pprint(items)
#     for item in items:
#         markets.append(
#             {
#                 'address': item.find('h4', class_='js-city-name').get_text(strip=True) +
#                            item.find('div', class_='shop-address').get_text(strip=True),
#                 'latlon': [item.find('div', class_='shop-list').find('div').get('data-shop-latitude'),
#                            item.find('div', class_='shop-list').find('div').get('data-shop-longitude')],
#                 'name': item.find('div', class_='shop-list').find('div').get('data-shop-name'),
#                 'phones': [item.find('div', class_='shop-phone').get_text(strip=True)],
#                 'working_hours': [item.find('div', class_='shop-weekends').get_text(strip=True),
#                                   item.find('div', class_='shop-work-time').get_text(strip=True)],
#             }
#         )
#         pprint(markets)
#     # with open('markets.json', 'w') as file:
#     #     json.dump(markets, file, indent=2, ensure_ascii=False)
#         return pprint(markets)
#
#
# html = get_html(URL)
# print(get_content(html.text))


# def write_json(markets):
#     try:
#         data = json.load(open('markets.json'))
#     except:
#         data = []
#     data.append(markets)
#     with open('markets.json', 'w') as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)


# def main():
#     html = get_html(URL)
#     get_content(html.text)
#
#
#
# if __name__ == '__main__':
#     main()




from bs4 import BeautifulSoup
import requests
import json


URL = 'https://www.mebelshara.ru/contacts/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='city-item')
    markets = []

    for item in items:
        markets.append(
            {
                'address': item.find('h4', class_='js-city-name').get_text(strip=True) +
                           item.find('div', class_='shop-address').get_text(strip=True),
                # 'latlon': [item.find('div', class_='shop-list').find('div').get('data-shop-latitude'),
                #            item.find('div', class_='shop-list').find('div').get('data-shop-longitude')],
                # 'name': item.find('div', class_='shop-list').find('div').get('data-shop-name'),
                # 'phones': [item.find('div', class_='shop-phone').get_text(strip=True)],
                # 'working_hours': [item.find('div', class_='shop-weekends').get_text(strip=True),
                #                   item.find('div', class_='shop-work-time').get_text(strip=True)],
            }
        )
    with open('markets.json', 'w') as file:
        json.dump(markets, file, indent=2, ensure_ascii=False)
        return markets

html = get_html(URL)
print(get_content(html.text))
