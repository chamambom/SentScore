from kafka import KafkaConsumer
import json

topic_name = 'twitterdata'
consumer = KafkaConsumer(topic_name,

                         bootstrap_servers=['20.87.42.17:9092'],
                         enable_auto_commit=True,
                         auto_offset_reset='smallest',
                         auto_commit_interval_ms =  5000,
                         fetch_max_bytes = 128,
                         max_poll_records = 100,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    tweets = json.loads(json.dumps(message.value))
    print(tweets)


