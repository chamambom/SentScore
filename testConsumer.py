from kafka import KafkaConsumer
topic_name = 'twitterdata'
consumer = KafkaConsumer(topic_name,
                     bootstrap_servers=['20.87.42.17:9092'],
                     group_id=None,
                     enable_auto_commit=True,
                     auto_offset_reset='smallest')

print("Consuming messages from the given topic")
for message in consumer:
    print("Message", message)
    if message is not None:
        print (message.offset, message.value)

print ("Quit")