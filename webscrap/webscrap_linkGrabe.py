import re
import linkGrabber
import ssl

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#url = "http://mhrd.gov.in"
url = "http://upfireservice.gov.in/"
links = linkGrabber.Links(url)
gb = links.find(duplicate=False)
count = 0
for rec in gb:
   url_text = rec['text']
   url_href = rec['href']
   if '.pdf' in url_href:
	count +=1
	if not url_href.startswith('http'):
	   url_href = url + url_href
	
	#print url_text
	print url_href
print count


