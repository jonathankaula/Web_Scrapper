
""" WEB SPIDER"""

import requests
from bs4 import BeautifulSoup
import csv
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
import threading

class Spider():


	def __init__(self,url):
		self.url = url


	def find_https(self,string):
	  
	    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	    url = re.findall(regex,string)      
	    return [x[0] for x in url]

	def get_links(self):

		
		r = requests.get(self.url)
		Content = BeautifulSoup(r.content,'html.parser')
		links = []
		Links= []
		for link in Content.find_all():
			links.append(link.get('href'))

		# Write non empty strings to list
		for i in links:
			if i != None:
				Links.append(i)
			http_ls = self.find_https(' '.join(Links))
			path = 'http.txt'
			# Write links to file
			with open(path,'w') as file:
				for i in http_ls:
					file.write('%s\n'% i)

		return http_ls






		



