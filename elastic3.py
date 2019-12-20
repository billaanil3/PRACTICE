from elasticsearch import Elasticsearch 
# Connect to the elastic cluster
#es=Elasticsearch([{'host':'localhost','port':9200}])
es = Elasticsearch()
#print es
e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}
#print e1
#Now let's store this document in Elasticsearch 
res1 = es.index(index='megacorp',doc_type='employee',id=1,body=e1)
#print res1
e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}
res2=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
print res2['_shards']

res3=es.get(index='megacorp',doc_type='employee',id=3)
print res3
res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)
#print res['created']

