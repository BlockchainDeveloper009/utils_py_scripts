
from yahoofinancials import YahooFinancials
apple = 'AAPL'
xela = 'XELA'
from_date =
ticker = xela
yahoo_financials = YahooFinancials(ticker)

balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
income_statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
all_statement_data_qt =  yahoo_financials.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
apple_earnings_data = yahoo_financials.get_stock_earnings_data()
apple_net_income = yahoo_financials.get_net_income()
historical_stock_prices = yahoo_financials.get_historical_price_data('2021-03-01', '2021-03-09', 'weekly')
historical_stock_prices = yahoo_financials.get_historical_price_data('2021-03-22', '2021-03-23', 'daily')

print('balance_sheet_data_qt')
print(balance_sheet_data_qt)
print('----------------')


print('income_statement_data_qt')
print(income_statement_data_qt)
print('----------------')
daily_Current_price = yahoo_financials.get_stock_price_data()

print('all_statement_data_qt')
print(all_statement_data_qt)
print('----------------')


print('apple_earnings_data')
print(apple_earnings_data)
print('----------------')

print('apple_net_income')
print(apple_net_income)
print('----------------')


print('historical_stock_prices')
print(historical_stock_prices)
print('----------------')


