from urllib.request import urlretrieve
#https://stackoverflow.com/questions/47928608/how-to-use-beautifulsoup-to-parse-google-search-results-in-python

import urllib.parse
from urllib.parse import urlencode, urlparse, parse_qs
import webbrowser
from bs4 import BeautifulSoup
import requests

address = 'https://google.com/#q='
# Default Google search address start
file = open( "OCR.txt", "rt" )
# Open text document that contains the question
word = file.read()
file.close()

myList = [item for item in word.split('\n')]
newString = ' '.join(myList)
# The question is on multiple lines so this joins them together with proper spacing

print(newString)

qstr = urllib.parse.quote_plus(newString)
# Encode the string

newWord = address + qstr
# Combine the base and the encoded query

print(newWord)

source = requests.get(newWord)

soup = BeautifulSoup(source.text, 'lxml')