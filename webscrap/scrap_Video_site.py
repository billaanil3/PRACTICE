import urllib2
from bs4 import BeautifulSoup as soup
import csv

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uclient = urllib2.urlopen(my_url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

file_name = "scrap_video.csv"
with open(file_name,"wb+") as f:
    headers = "Brand , Product_Name, Shipping\n"
    f.write(headers)

    for container in containers:
        brand = container.div.div.a.img['title']
        title_container = container.findAll('a',{"class":"item-title"})
        print title_container[0].text
        product_name = title_container[0].text
        shipping_container = container.findAll("li",{"class":"price-ship"})
        shipping = shipping_container[0].text.strip()

        # print ("Brand:" +brand)
        # print ("Product-Name:" +product_name)
        # print ("Shipping :" +shipping)

        f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")
    f.close()