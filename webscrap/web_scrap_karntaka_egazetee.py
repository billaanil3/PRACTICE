import ssl
import urllib2
import requests
from bs4 import BeautifulSoup
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

#--------------------------------------------------------------------------------
# url = "https://www.gazette.kar.nic.in"
# url = "http://labour.and.nic.in/"
url = "http://ls1.and.nic.in/Industry/Home.php"
page = urllib2.urlopen(url,context = gcontext)
# page = urllib2.urlopen("https://www.cdslindia.com/publications/latestnews.html")
# page = urllib2.urlopen('http://www.python.org/')
soup = BeautifulSoup(page.read(),"lxml")

links = soup.find_all('table',width="340")
# print links
for link in links:
    for rec in link.find_all('a'):
        if '.pdf' in rec['href']:
            print rec['href']
#----------------------------------------------------------------------------------
# url = "http://www.arunachalpradesh.gov.in/gazette/"
# page = urllib2.urlopen(url,context = gcontext)
# # print page
# soup = BeautifulSoup(page.read(),"lxml")
# # print soup
# links = soup.find_all('div',class_="tab-content")
# target_list = []
# for link in links:
#     target_content = ''
#     target_url = ''
#     for rec in link.find_all('tr'):
#         element_dictionary = dict()
#         for a in rec.find_all('td',width="30%"):
#             target_content = a.text
#         for pdfs in rec.find_all('td'):
#             for pdf in pdfs.find_all('a'):
#                 target_url = pdf['href']
#                 element_dictionary['target_content'] = target_content
#                 element_dictionary['target_url'] = target_url
#                 target_list.append(element_dictionary)
# print target_list
 #-----------------------------------------------------------------------------
 # url = "http://govtpress.odisha.gov.in/view.asp?id=18"
 # page = urllib2.urlopen(url)       