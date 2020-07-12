import urllib.request
import requests
from bs4 import BeautifulSoup
url ='http://quotes.toscrape.com/' #pour selectioner le site de travail
#url = str(input("entrer le site a traiter Merci : "))
response = urllib.request.urlopen(url)
html_data = response.read()
soup = BeautifulSoup(html_data, 'html.parser')
#print(soup.find('title').text) #pour recuperer le titre 
print(soup.find('a').get('href'))#pour recuperer l'url 
#for hrefs in soup.findAll('a'):
#	print(hrefs.get('href')) #pour recuperer tous les urls 
#for i in soup.findAll('h2'):
#	print(i.strong) #pour recuperer les titres H2  et gras 
#for i in soup.findAll('h2'):
#	print(i.text) #pour recuperer le text de tous les titres H2  et gras 
#for i in soup.findAll('img',{"class":"W(100%) Mih(215px) Mih(277px)--miw1200","alt":""}):
	#print(i.get('src')) #pour recuperer l'image avec son nom et sa taille  
    #url_img = (i.get('src')) 
    #img_name = url_img.split("/")[-1]
    #print("downloading {0}".format(img_name)) 
    #response_img = requests.get(i.get("src"))
    #data = response_img.content
    #file = open(img_name,"wb")
    #file.write(data)
    #file.close 
from selenium import webdriver
driver=webdriver.C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome()
driver.get('https://facebook.com')



#from bs4 import BeautifulSoup as BS
#import requests as rq
#url ='http://quotes.toscrape.com/'
#s = BS(url,'html,parser')
#thing = s.find('a')
#print(thing.find('a').get('href'))
