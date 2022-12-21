import requests	#download html
from bs4 import BeautifulSoup	#html->data

res= requests.get('https://news.ycombinator.com/')
print(res)