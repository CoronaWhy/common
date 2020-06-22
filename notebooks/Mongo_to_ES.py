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
    actions.append(data)
    
# Delete v22papers index if it exists
try:
    delete = es.indices.delete(index = 'v22papers')
except Exception as e:
    print(e)
    
# Set up the shards and mappings for the data
request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings" : {
        "properties" : {
            "who_covidence_id" : { "type" : "text" },
            "source_x" : { "type" : "text" },
            "pmcid" : { "type" : "text" },
            "pubmed_id" : { "type" : "text" },
            "license" : { "type" : "text" },
            "publish_time" : { "type" : "text" },
            "authors" : { "type" : "text" },
            "journal" : { "type" : "text" },
            "mag_id" : { "type" : "text" },
            "arxiv_id" : { "type" : "text" },
            "s2_id" : { "type" : "text" },
            "year" : { "type" : "text" },
            "path" : { "type" : "text" },
            "cord_uid" : { "type" : "text", "index" : True },
            "title" : { "type" : "text" },
            "abstract.text" : { "type" : "text" },
            "abstract.cite_spans.start" : { "type" : "long" },
            "abstract.cite_spans.end" : { "type" : "long" },
            "abstract.cite_spans.text" : { "type" : "text" },
            "abstract.cite_spans.ref_id" : { "type" : "text" },
            "abstract.ref_spans.start" : { "type" : "long" },
            "abstract.ref_spans.end" : { "type" : "long" },
            "abstract.ref_spans.text" : { "type" : "text" },
            "abstract.ref_spans.ref_id" : { "type" : "text" },
            "abstract.section" : { "type" : "text" },
            "body_text.text" : { "type" : "text" },
            "body_text.cite_spans.start" : { "type" : "long" },
            "body_text.cite_spans.end" : { "type" : "long" },
            "body_text.cite_spans.text" : { "type" : "text" },
            "body_text.cite_spans.ref_id" : { "type" : "text" },
            "body_text.ref_spans.start" : { "type" : "long" },
            "body_text.ref_spans.end" : { "type" : "long" },
            "body_text.ref_spans.text" : { "type" : "text" },
            "body_text.ref_spans.ref_id" : { "type" : "text" },
            "body_text.section" : { "type" : "text" },
            "tables" : { "type" : "text" },
            "body_rows.cord_uid" : { "type" : "text" },
            "body_rows.section" : { "type" : "text" },
            "body_rows.subsection" : { "type" : "text"},
            "body_rows.text" : { "type" : "text" }
        }
    }
}

# Create ElasticSearch index
es.indices.create(index='v22papers', body = request_body, ignore=400)

# Inserting data to ElasticSearch instance
for i in tqdm(range(0, len(actions))):
    try:
        actions[i]['pubmed_id'] = str(actions[i]['pubmed_id'])     # Some transformations to escape mapping conflicts
        for j in actions[i]['body_rows']:
            j['text'] = str(j['text'])
            j['subsection'] = str(j['subsection'])
        res = es.index(index = 'v22papers', body = actions[i])
    except Exception as e:
        print("Error in index {}, {} : {}".format(i, actions[i]['cord_uid'], e))

es.indices.refresh(index="v22papers")

# Check for number of documents in v22papers index
print(es.cat.indices())
