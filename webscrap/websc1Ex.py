from websc1 import simple_get
import pdb
pdb.set_trace()
raw_html = simple_get('https://realpython.com/blog/')
len(raw_html)
no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
if no_html:
   print "True" 
