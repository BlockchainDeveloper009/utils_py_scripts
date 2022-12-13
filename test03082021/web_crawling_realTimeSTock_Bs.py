import bs4
import requests


stocks_dict = {
    "FB": {
        "URL": "https://finance.yahoo.com/quote/FB?p=FB"
    },
    "APPL": {
        "URL": "https://finance.yahoo.com/quote/FB?p=FB"
    }
}


def parsePrice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
        #.find('span').text
    return price


while True:
    print(parsePrice())
