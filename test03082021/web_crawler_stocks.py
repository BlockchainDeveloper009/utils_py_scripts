#Yahoo Finance
#https://www.youtube.com/watch?v=fw4gK-leExw
import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

S1 = 'FORD'
S2 = 'F'
url_stats = 'https://finance.yahoo.com/quote/{S1}/key-statistics?p={S1}'
url_profile= 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'F'

response = requests.get(url_financials.format(stock,stock))
soup = BeautifulSoup(response.text,'html.parser')

pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])

json_data['context'].keys()
json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys()

annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quarterly_is= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']

annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quarterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']


print(annual_is[0])