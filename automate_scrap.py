import requests
from bs4 import BeautifulSoup

url = "https://dgps.gujarat.gov.in/webcontroller/page/government-resolutions"
req = requests.get(url)
soup = BeautifulSoup(req.content)
links = soup.find_all('a')
# print links

for link in links:
    # print "*****************",link.get('href')
    # print "#################",str(link.text())
    if '.pdf' in link.get('href'):
        wrapper = link.parent.parent.parent.parent
        print wrapper.has_attr('class')
