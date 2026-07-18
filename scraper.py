import bs4
import urllib.request
import re

prices_list = [] # stores the price of the game in a list
def check_price():
    url = "https://store.steampowered.com/app/1297900/Gothic_1_Remake/"

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, 'html.parser')

    price_div = soup.find('div', class_='game_purchase_price price')

    if price_div:
        price_text = price_div.text.strip()
        price_clean = re.sub(r'[^\d.]', '', price_text)  # removes any non-number characters except the decimal point
        price = float(price_clean)
        print(price, type(price))
    else:
        print("Price not found.")

check_price()