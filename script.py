import requests
import subprocess
from optparse import *
import re

def get_arguments():
	parser = OptionParser()
	parser.add_option('-s', '--site', dest='site_url', help='Site that you are want to parse.')
	(options, arguments) = parser.parse_args()
	return options

def get_request(options):
	request = requests.get(options.site_url)
	return request

options = get_arguments()

g1 = re.findall(r'(((https|http):\/\/)([\w\d]+))', options.site_url)

t1 = get_request(options)

# p1 = r"(((https|http):\/\/)[\w+.\-\d\/]+(\?)[\w\=\&]+)"

p1 = r"((((https|http):\/\/)[\w+.]+)[\w+.\-\d\/]+(\?)[\w\=\&%]+)"

u1 = re.findall(p1, t1.text)

# print(options.site_url)


#print(g1[0][3])
#print(i[1])


for i in u1:
	if ((g1[0][3] in i[1]) & ('.css?' not in i[0]) & ('.js?' not in i[0])):
		print ( i[0] )
