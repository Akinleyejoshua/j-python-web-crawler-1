from urllib import request
goog_url = 'http://www.C360IT.wordpress.com'
def web_data(data_url):
	response = request.urlopen(data_url)
	data = response.read()
	data_str = str(data)
	lines = data_str.split('\\n')
	dest_url = r'goog_url'
	fx = open('dest_url', 'w')
	for line in lines:
		print(line + '\n')
web_data(goog_url)