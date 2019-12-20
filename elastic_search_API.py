import requests
import json

def search(uri,term):
    """Simple Elastic search query"""
    print uri
    query = {"query":{"match":{"Uploaded By.placeholder":term}}}
    response = requests.get(uri)
    # print response
    results = json.loads(response.text)
    return results

def format_results(results):
    """print results nicely :(doc_id) content"""
    # print results
    data = [doc for doc in results['hits']['hits']]
    # print data
    for doc in data:
        # print(doc.keys())
        if 'Uploaded By' in doc['_source']:
            # x = json.dumps(doc['_source']['Uploaded By'])
            # print x
            print("%s) %s" % (doc['_id'], json.dumps(doc['_source']['Uploaded By']['placeholder'])))
            # print("%s) %s" % (doc['_id'], doc['_source']['Force Majure']))

    # for key,value in results.items():
    #     doc_dict = {key:value}
    #     for doc in doc_dict['hits']['hits']:
    #         print (doc['_source'])
    #         print("%s) %s" % (doc['_id'], doc['_source']['Uploaded By']))
def create_doc(uri,doc_data = {}):
    """Create new document."""
    query = json.dumpa(doc_data)
    response = requests.post(uri,data = query)
    print response

if __name__ == '__main__':
    uri_search = 'http://localhost:9200/_search'
    # uri_create = 'http://localhost:9200/test-index/tweet/'

    results = search(uri_search,"Uploaded By")
    # print results
    format_results(results)
