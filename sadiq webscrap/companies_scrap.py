import ssl
import urllib2
from bs4 import BeautifulSoup
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
url = "https://www.ambitionbox.com/overview?utm_source=naukri&utm_medium=gnb"
companies_list = []
input_comp_name = "Accenture"
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req, context=gcontext)
    if page:
        soup = BeautifulSoup(page.read(), "lxml")
        links = soup.find_all('div', class_="companies_tiles_wrap")
        for link in links:
            companies = link.find_all("p", class_="company_name")
            for comp in companies:
                # companies_list.append(str(comp.text))
                if str(comp.text) == input_comp_name:
                    print "--------------", comp.text
                    print link.find_all('div', class_="company_tile_btn")
                    # company_data = comp.find_all("a")
            # print link.find_all('a', title_=input_comp_name + str(overview))
            # print link.find_all('a', attrs={"title": input_comp_name})

        # print companies_list
        #
        # # if "input_comp_name" in companies_list:
        # print "input_comp_name", input_comp_name
        # for link in links:
        #     print link.find_all("a", title_=input_comp_name)
        # print comp_links
        # companies_list = dict(res=companies_list)
except Exception:
        print "ERROR:The site can't be reached."
