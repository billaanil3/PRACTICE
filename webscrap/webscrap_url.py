import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://mhrd.gov.in/")
soup = BeautifulSoup(page,"lxml")

records = soup.find_all('a')
#print records
for rec in records:
   print type(rec['href'])
