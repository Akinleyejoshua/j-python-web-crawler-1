import requests
from bs4 import beautifulSoup4


def web_spider(max_pages):
	page = 1
	page += 1
	while page <= max_pages:
		url = 'http://abc/php?page=' + str(page)
		source_code = request.get(url)
		plain_text = source_code.text
		soup = beautifulSoup(plain_text)
		for link in soup.findAll('a', {'class': 'item-name'}):
			href = 'http://abc.com' + link.get('href')
			print(href)
web_spider(1)
