import requests
import subprocess
from optparse import *
import re

def get_arguments():
	parser = OptionParser()
	parser.add_option('-s', '--site', dest='site_url', help='Site that you want to parse.')
	(options, arguments) = parser.parse_args()
	return options

def get_request(options):
	request = requests.get(options.site_url)
	return request

options = get_arguments()

t1 = get_request(options)

p1 = r"(((https|http):\/\/)[\w+.\-\d\/]+(\?)[\w\=\&]+)"

u1 = re.findall(p1, t1.text)

for i in u1:
	print( i[0] )

