from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
file = open("Elastic_json.json",'r')
data = file.read()
print type(data)
data = []
data.append({"One":1})
data.append({"two":2})

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
counter =1
for d in data:
    res = es.index(index="test-index", doc_type='tweet', id=counter, body=d)
    counter += 1
res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
#for hit in res['hits']['hits']:
 #   print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
