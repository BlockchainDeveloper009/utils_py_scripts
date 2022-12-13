import yfinance as yf

class Test:
    def __init__(self, speed=0):

        msft = yf.Ticker("MSFT")
        print(msft)
        print(msft.info)

        all_stocks = [yf.Ticker("MSFT"), yf.Ticker("NSP"),yf.Ticker("BLM")]
        for t in all_stocks:
            print('Dividens'+t.dividends)
            #print('hist = '+t.history(period="5d"))



"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""
if __name__ == '__main__':
    my_car = Test()
    print("I'm a car!")



"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}"""