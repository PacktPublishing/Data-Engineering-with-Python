from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

fake=Faker()
es = Elasticsearch() #or pi {127.0.0.1}

doc={"name": fake.name(),"street": fake.street_address(), "city": fake.city(),"zip":fake.zipcode()}


res=es.index(index="users",doc_type="doc",body=doc)
print(res)



doc={"query":{"match":{"_id":"pDYlOHEBxMEH3Xr-2QPk"}}}
res=es.search(index="users",body=doc,size=10)
print(res)

