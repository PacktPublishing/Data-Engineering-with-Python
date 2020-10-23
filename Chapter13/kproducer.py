from confluent_kafka import Producer
from faker import Faker
import json
import time

fake=Faker()

p=Producer({'bootstrap.servers':'localhost:9092,localhost:9093,localhost:9094'})

#p.list_topics().topics



def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        print("{} : Message on topic {} on partition {} with value of {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msg.timestamp()[1]/1000)), msg.topic(), msg.partition(), msg.value().decode('utf-8')))

for i in range(10):
    data={"name":fake.name(),"age":fake.random_int(min=18, max=80, step=1),"street":fake.street_address(),"city":fake.city(),"state":fake.state(),"zip":fake.zipcode()}
    m=json.dumps(data)
    p.poll(0)
    p.produce('users',m.encode('utf-8'),callback=receipt)

p.flush()

