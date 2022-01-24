from bs4 import BeautifulSoup
import requests
import csv


CSV = 'cards.csv'
HOST = 'https://minfin.com.ua/'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-item')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='title').get_text(strip=True),
                'link_product': HOST + item.find('div', class_='title').find('a').get('href'),
                'brand': item.find('div', class_='brand').get_text(strip=True),
                'card_img': HOST + item.find('div', class_='image').find('img').get('src')

            }
        )
    return cards

html = get_html(URL)
print(get_content(html.text))



def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название продукта', 'Ссылка на продукт', 'Банк', 'Изображение карты'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['brand'], item['card_img']])

def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
            pass
    else:
        print('Error')

parser()























# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     result = requests.get(url)
#     return result.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     h1 = soup.find('h1', {'class': 'page-header__info-title'})
#     a = soup.find('a', {'href': 'https://habr.com/ru/post/461939/'})
#     navbar = soup.find('ul', {'id': 'navbar-links'})
#     li = navbar.find('li').find('a').text
#     print(li)
#
#
# def main():
#     html = get_html('https://habr.com/ru/hub/python/')
#     get_data(html)
#
#
# if __name__ == '__main__':
#     main()
