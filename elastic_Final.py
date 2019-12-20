from datetime import datetime
from elasticsearch import Elasticsearch
import json
es = Elasticsearch()
file = open("Elastic_json.json",'r')
data = file.read()
#print type(data)
dict_data = json.loads(data)
#print (dict_data)
counter =1
for key,value in dict_data.items():
    my_dat = {key:value}
    res = es.index(index="test-index", doc_type='tweet', id=counter, body=my_dat)
    counter += 1
query = {"query":{"match":{"Uploaded By.placeholder":"Uploaded By"}}}

res = es.search(index="test-index", doc_type='tweet', body=query)
print res
print("%d documents found:" % res['hits']['total'])
for doc in res['hits']['hits']:
   print("%s) %s" % (doc['_id'], doc['_source']['Uploaded By']))
#res = es.delete(index="test-index",doc_type='tweet', id=counter)
