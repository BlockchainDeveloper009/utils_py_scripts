from yahoofinancials import YahooFinancials

from JsonToCsv import write_to_csv

tech_stocks = ['AAPL', 'MSFT', 'INTC']
bank_stocks = ['WFC', 'BAC', 'C']
commodity_futures = ['GC=F', 'SI=F', 'CL=F']
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
us_treasuries = ['^TNX', '^IRX', '^TYX']

yahoo_financials_tech = YahooFinancials(tech_stocks)
yahoo_financials_banks = YahooFinancials(bank_stocks)
yahoo_financials_commodities = YahooFinancials(commodity_futures)
yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
yahoo_financials_currencies = YahooFinancials(currencies)
yahoo_financials_mutualfunds = YahooFinancials(mutual_funds)
yahoo_financials_treasuries = YahooFinancials(us_treasuries)

tech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('annual', 'cash')
bank_cash_flow_data_an = yahoo_financials_banks.get_financial_stmts('annual', 'cash')

banks_net_ebit = yahoo_financials_banks.get_ebit()
tech_stock_price_data = yahoo_financials_tech.get_stock_price_data()
daily_bank_stock_prices = yahoo_financials_banks.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_commodity_prices = yahoo_financials_commodities.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_currency_prices = yahoo_financials_currencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_mutualfund_prices = yahoo_financials_mutualfunds.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_treasury_prices = yahoo_financials_treasuries.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
daily_Current_price = yahoo_financials.get_stock_price_data()
print('banks_net_ebit')
print(banks_net_ebit)
print('----------------')

print('tech_stock_price_data')
print(tech_stock_price_data)
print('----------------')

print('daily_bank_stock_prices')
print(daily_bank_stock_prices)
print('----------------')

print('daily_commodity_prices')
print(daily_commodity_prices)
print('----------------')

print('daily_crypto_prices')
print(daily_crypto_prices)
print('----------------')


print('daily_currency_prices')
print(daily_currency_prices)
print('----------------')


print('daily_mutualfund_prices')
print(daily_mutualfund_prices)
print('----------------')


print('daily_treasury_prices')
print(daily_treasury_prices)
print('----------------')



