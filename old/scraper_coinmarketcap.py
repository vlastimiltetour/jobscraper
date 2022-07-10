from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

tbody = soup.tbody
trs = tbody.contents


prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

for n, p in prices.items():
    print(n, p)


