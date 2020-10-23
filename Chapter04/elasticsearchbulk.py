from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

fake=Faker()
es = Elasticsearch() #or pi {127.0.0.1}

actions = [
  {
    "_index": "users",
    "_type": "doc",
    "_source": {
	"name": fake.name(),
	"street": fake.street_address(), 
	"city": fake.city(),
	"zip":fake.zipcode()}
  }
  for x in range(998) # or for i,r in df.iterrows()
]

response = helpers.bulk(es, actions)
print(response)

