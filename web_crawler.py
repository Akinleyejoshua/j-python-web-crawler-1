import random
import urllib.request

def download_web_app(url):
	name = random.randrange(1, 100)
	full_name = str(name) + '.exe'
	urllib.request.urlretrieve(url, full_name)
	'''
download_web_app('http://www.abc.com')
'''
