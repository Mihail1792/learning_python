import requests
import re
from pprint import pprint

r = requests.get("https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=5060&tt=1&vtb=v.or%3A39&vtt=v.or%3A5&vtd=v.or%3A37")
matches = re.findall(r'<script id="__NEXT_DATA__" type="application/json">.+?</script>', r.text)

parsed = re.findall(r'https://www.kufar.by/item/\d{9}', r.text)
b = {}
page_link = 0
for item in parsed:
    page_link += 1
    b.update({(page_link): item})
z = b.values()
print(z)





# from bs4 import BeautifulSoup
# import requests
#
# HOST = 'https://www.kufar.by/'
# URL = 'https://www.kufar.by/listings?size=42&sort=lst.d&cur=BYR&cat=5060&rgn=7&tt=1&vtb=v.or%3A39&vtt=v.or%3A5&vtd=v.or%3A37'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
# }
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='kf-aJNC-5291d')
#     tv = []
#     for item in items:
#         tv.append(
#             {
#                 'title': item.find('h3', class_='kf-SeNG-42621').get_text(),
#                 'price': item.find('div', class_='kf-SNyn-8ae6f').get_text(),
#                 'link_page': HOST + item.find('div', class_='kf-aQaE-c2a7c').find('a').get('href'),
#                 'location': item.find('span', class_='kf-SPbA-da912').get_text(),
#                 'img': item.find('div', class_='kf-avsj-8f445').find('img').get('src')
#             }
#         )
#     return tv
#
# html = get_html(URL)
# print(get_content(html.text))



# войти в реддис и по каждому ЮРЛ сверить с реддисом и если нет отослать в телегу и сохранить в реддис в
# цикле фор по ключу забрать сохранить в реддис