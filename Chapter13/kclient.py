from confluent_kafka import Consumer

c=Consumer({'bootstrap.servers': 'localhost:9092,localhost:9093,localhost9093','group.id':'python-consumer','auto.offset.reset':'earliest'})

t=c.list_topics()
t.topics

#{'people': TopicMetadata(people, 1 partitions), '__transaction_state': TopicMetadata(__transaction_state, 50 partitions), 'users': #TopicMetadata(users, 3 partitions), 'dataengineering': TopicMetadata(dataengineering, 1 partitions), '__consumer_offsets': #TopicMetadata(__consumer_offsets, 50 partitions)}

t.topics['users'].partitions

#{0: PartitionMetadata(0), 1: PartitionMetadata(1), 2: PartitionMetadata(2)}

c.subscribe(['users'])

while True:
    msg=c.poll(1.0) #timeout

    if msg is None:
        continue
   
    if msg.error():
        print("Error: {}".format(msg.error()))
        continue

    data=msg.value().decode('utf-8')
    print(data)
c.close()

