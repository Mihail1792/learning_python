# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
# import re
#
# URL = 'https://www.tvoyaapteka.ru/adresa-aptek/'
#
#
# def get_html(url, headers='', params=''):
#     response = requests.get(url, headers=headers, params=params)
#     return response
#
#
# def get_city(html):
#     global item
#     soup = BeautifulSoup(html, 'html.parser')
#     # items = soup.find_all('span', class_='col-xs-12')
#     # region = []
#     # for item in items:
#     #     region.append(
#     #         {
#     #             'region': item.get_text(strip=True),
#     #         }
#     #     )
#     # pprint(region)
#     my_city = soup.find_all('a', class_='col-xs-12 town_xs_item town')
#     city = []
#     for i in my_city:
#         id = i.get('data-id')
#         if id is not None:
#             city.append(id)
#     return city
#
# def get_content(html):
#     global item, t
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='apteka_info')
#     pharmacy = []
#     for item in items:
#         phones = soup.find('div', class_='phone').get_text(strip=True)  # ищет телефон общий для всех
#         t = re.findall(r'\d{1}-\d{3}-\d{3}-\d{3}', phones)  # с помощью регулярки вытягивает из полученного текста телефон
#
#         pharmacy.append(
#             {
#                 'adress': item.find('div', class_='apteka_address').get_text(strip=True),
#                 'name': item.find('div', class_='apteka_title').get_text(strip=True),
#                 'phones': t
#             }
#         )
#
#
#     latlons = soup.find_all('div', class_='apteka_item normal_store')  # ищет латлон аптек в отдельном цикле
#     latlons_list = []
#     for latlon in latlons:
#         latlons_list.append(
#             {
#                 'latlon': [latlon.get('data-lat'), latlon.get('data-lon')],
#             }
#         )
#     return pharmacy, latlons_list
#
# def collector_of_results(pharmacy, latlons_list):
#     result_list = []
#     for i in range(len(pharmacy)):
#         result_list.append({**pharmacy[i], **latlons_list[i]})
#
#     return result_list
#
#
# # html = get_html(URL)
# # pprint(get_content(html.text))
# # pprint(get_city(html.text))
#
#
# def parser(city_list):
#     for city in city_list:
#         HEADERS = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#             'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
#             'Cookie': f'BITRIX_SM_S_CITY_ID={city}; ''tmr_reqNum=304; ct_pointer_data=%5B%5B298%2C456%2C86%5D%2C%5B241%2C467%2C285%5D%2C%5B241%2C477%2C340'
#                       '%5D%2C%5B320%2C460%2C492%5D%2C%5B417%2C369%2C639%5D%2C%5B513%2C368%2C1186%5D%2C%5B513%2C369%2C1381%5D'
#                       '%2C%5B513%2C488%2C1450%5D%2C%5B558%2C593%2C1584%5D%2C%5B568%2C600%2C1892%5D%2C%5B825%2C374%2C551753%5D'
#                       '%2C%5B709%2C415%2C551796%5D%2C%5B345%2C614%2C551948%5D%2C%5B296%2C559%2C552095%5D%2C%5B244%2C420'
#                       '%2C552507%5D%2C%5B244%2C406%2C552547%5D%2C%5B311%2C339%2C552698%5D%2C%5B408%2C287%2C552852%5D%2C%5B472'
#                       '%2C301%2C552998%5D%2C%5B476%2C336%2C553167%5D%2C%5B476%2C336%2C553363%5D%2C%5B470%2C350%2C553451%5D%2C'
#                       '%5B114%2C309%2C557423%5D%2C%5B124%2C313%2C557526%5D%2C%5B126%2C315%2C557681%5D%2C%5B116%2C313%2C559160'
#                       '%5D%2C%5B202%2C333%2C559220%5D%2C%5B342%2C373%2C559373%5D%2C%5B363%2C397%2C559519%5D%2C%5B366%2C405'
#                       '%2C559909%5D%2C%5B381%2C424%2C559971%5D%2C%5B392%2C437%2C560124%5D%2C%5B392%2C438%2C560878%5D%2C%5B392'
#                       '%2C438%2C560879%5D%2C%5B388%2C557%2C561029%5D%2C%5B310%2C591%2C561182%5D%2C%5B286%2C632%2C561335%5D%2C'
#                       '%5B272%2C659%2C562013%5D%2C%5B334%2C517%2C562086%5D%2C%5B432%2C387%2C562239%5D%2C%5B473%2C371%2C565485'
#                       '%5D%2C%5B610%2C413%2C565574%5D%2C%5B542%2C432%2C565702%5D%2C%5B489%2C433%2C565855%5D%2C%5B418%2C502'
#                       '%2C571338%5D%2C%5B197%2C502%2C571377%5D%2C%5B117%2C500%2C571530%5D%5D; '
#                       'PHPSESSID=s0g82s26kg9ahebdg07ri3jdd8; '
#                       'ct_cookies_test=%7B%22cookies_names%22%3A%5B%22ct_timestamp%22%2C%22ct_prev_referer%22%5D%2C'
#                       '%22check_value%22%3A%2259466bbd500391cb399da083d7b3e175%22%7D; '
#                       'ct_prev_referer=https%3A%2F%2Fwww.tvoyaapteka.ru%2Fadresa-aptek%2F; ct_timestamp=1624388411; '
#                       'ct_fkp_timestamp=1624388406; _ga_HLYRZD8M17=GS1.1.1624387847.17.1.1624387867.40; '
#                       '_ga=GA1.2.777230343.1623704767; _gid=GA1.2.713269787.1624222700; tmr_detect=0%7C1624387855621; '
#                       '_fbp=fb.1.1623704767646.389705331; __utma=202854356.777230343.1623704767.1624371892.1624387853.16; '
#                       '__utmb=202854356.1.9.1624387853; __utmc=202854356; '
#                       '__utmz=202854356.1624320446.14.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=('
#                       'not%20provided); _ym_isad=2; tmr_lvid=e007b8fd11151fc2ceeeedc7c4fa28f2; tmr_lvidTS=1623704767665; '
#                       'ct_checkjs=3424e6e2e9d20d50f844f0843bef1f30; ct_timezone=3; ct_ps_timestamp=1624387852; '
#                       'ct_visible_fields=0; ct_visible_fields_count=0; BX_USER_ID=3f3dd8393f32c374bad1165713a22d59; '
#                       '_ym_d=1624312419; _ym_uid=1623704767201348384; BITRIX_SM_SALE_UID=3565043; '
#                       'BITRIX_SM_SP_deviceId=2021-06-15_06%3A06%3A05_d6ac1ecaf36e91c77839e1fbbf844730; '
#                       'BITRIX_SM_GEOIP=a%3A2%3A%7Bs%3A7%3A%22inetnum%22%3Bs%3A27%3A%2237.212.0.0+-+37.215.255.255%22%3Bs%3A7'
#                       '%3A%22country%22%3Bs%3A2%3A%22BY%22%3B%7D; '
#                       'BITRIX_SM_H2O_COOKIE_USER_ID=96e14b4033658120b2ae92b280267810; BITRIX_SM_LAST_IP=37.214.29.146 '
#         }
#
#         for _ in HEADERS:
#             # pprint(HEADERS.get(head))
#             html = get_html(URL, headers=HEADERS)
#         get_content(html.text)
#         pharmacy, latlons_list = (get_content(html.text))
#         pprint(collector_of_results(pharmacy, latlons_list))
#
#
# html = get_html(URL)
# get_content(html.text)
# city_list = get_city(html.text)
# pprint(city_list)
# parser(city_list)
































result_list = [{'adress': 'Минск'}, {'adress': 'Червень'}, {'adress': 'Гомель'}]
latlon_list = [{"latlon": [62.031799, 129.754762]}, {"latlon": [42.031566, 229.754987]}, {"latlon": [76.03656, 54.876756]}]

result = [{**x, **y} for x, y in zip(result_list, latlon_list)]
# print(result)

# print('abca'.strip('ac'))  # 'b'
# print('abca\n \t'.strip(' '))  # 'abca'



import re

a = "МишаСаша, 8:00"
result = re.split(r'\w\w\w\w', a)
print(result)




# result_list = [{'adress': 'Минск'}, {'adress': 'Червень'}, {'adress': 'Гомель'}]
# latlon_list = [{"latlon": [62.031799, 129.754762]}, {"latlon": [42.031566, 229.754987]}, {"latlon": [76.03656, 54.876756]}]
#
#
# list_1 = [{'adress': 'Минск'}, {'adress': 'Червень'}, {'adress': 'Гомель'}]
# list_2 = [{"latlon": [62.031799, 129.754762]}, {"latlon": [42.031566, 229.754987]}, {"latlon": [76.03656, 54.876756]}]
# list_3 = []
# for i in range(len(list_1)):
#     list_3.append({**list_1[i],**list_2[i]})
# print(list_3)


# [
# 	{
# 	 "address": "203-й  микрорайон, корп. 1",
# 	 "latlon": [62.031799, 129.754762],
# 	 "name": "ТвояАптека.рф",
# 	 "phones": [ "+78001000003"],
# 	 "working_hours": ["пн-вс 08:00-21:00"]
#   	  }
# ]










# alfabet_list = ['a', 'b', 'c', 'd', 'i', 'f', 'g']
# word_list = ['dog', 'salt', 'cat', 'milk', 'beer', 'world', 'hello']


# d = [[1,2,3],[4,5,6]]
# result_list = []
# for i in range(2):
#     for j in range(3):
#         result_list.append(
#             {
#                 '1': (i, j)
#             }
#         )
#         print(result_list)


