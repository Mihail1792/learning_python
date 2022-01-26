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



# войти в реддис и по каждому ЮРЛ сверить с реддисом и если нет отослать в телегу и сохранить в реддис в
# цикле фор по ключу забрать сохранить в реддис


