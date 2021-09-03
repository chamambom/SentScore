from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='20.87.42.17:9092') #Same port as your Kafka server

"""API ACCESS KEYS"""
access_token = "25076010-uCDmucxKYDNaYQ9HDDcS6iWdaZnbv4L5q8Aii72Xe"
access_token_secret = "CNqLk6hRx9XXOosr989KR9GiTRceMP24sVzi8fRT21UQs"
consumer_key = "QYpq7ooIqCoDHPD8eUFSRcNiJ"
consumer_secret = "Z3OesLBi8dn7uRP9b7mDnlRAaLgVoQtez9BnJbFRnzhTVPgOl8"

topic_name = "twitterdata"



class twitterAuth():
    """SET UP TWITTER AUTHENTICATION"""
    def authenticateTwitterApp(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth



class TwitterStreamer():
    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self):
        while True:
            listener = ListenerTS()
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=["Python"], stall_warnings=True, languages= ["en"])


class ListenerTS(StreamListener):
    def on_data(self, raw_data):
            producer.send(topic_name, str.encode(raw_data))
            return True

if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()