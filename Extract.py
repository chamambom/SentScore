from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json

access_token = "25076010-uCDmucxKYDNaYQ9HDDcS6iWdaZnbv4L5q8Aii72Xe"
access_token_secret = "CNqLk6hRx9XXOosr989KR9GiTRceMP24sVzi8fRT21UQs"
consumer_key = "QYpq7ooIqCoDHPD8eUFSRcNiJ"
consumer_secret = "Z3OesLBi8dn7uRP9b7mDnlRAaLgVoQtez9BnJbFRnzhTVPgOl8"

class StdOutListener(StreamListener):
    def on_data(self, data):
        json_ = json.loads(data)
        producer.send("basic", json_["text"].encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(bootstrap_servers='20.87.42.17:9092')
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=["covid19", "corona virus"])
