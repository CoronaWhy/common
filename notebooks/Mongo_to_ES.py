# Installing ElasticSearch and MongoDB wrapper
import os
os.system('pip install elasticsearch==7.6.0')
os.system('pip install pymongo')

# Import relevant libraries
import json
import requests 
from tqdm import tqdm
from elasticsearch import helpers, Elasticsearch
from pymongo import MongoClient

# Set connections
es = Elasticsearch("http://elastic:changeme@search.coronawhy.org:80/", Port=80)
mongouser = 'coronawhyguest'
mongopass = 'coro901na'
cordversion = 'v22'
client = MongoClient("mongodb://%s:%s@mongodb.coronawhy.org" % (mongouser, mongopass))
db = client.get_database('cord19')

# Pull from mongodb 
actions = []
for data in tqdm(db.v22.find(), total=db.v22.estimated_document_count()):
    data.pop('_id')
    action = {
            "index": {
                    "_index": 'v22papers',
                    "_type": '_paper',
                    }
    }
    actions.append(action)
    actions.append(data)

# Dump into ES using Bulk API
delete = es.indices.delete(index = 'v22papers')
request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
es.indices.create(index='v22papers', body = request_body, ignore=400)

# Uploading in splits so it doesn't consume much RAM
res = es.bulk(index = 'v22papers', body = actions[:200], refresh = True, request_timeout=50) 
j = 200
for i in tqdm(range(400, 52400, 200)):
    prev = j
    res = es.bulk(index = 'v22papers', body = actions[prev:i], refresh = True, request_timeout=50)
    j = i
res = es.bulk(index = 'v22papers', body = actions[52400:], refresh = True, request_timeout=50)

# Check for number of documents in v22papers index
print(es.cat.indices())
