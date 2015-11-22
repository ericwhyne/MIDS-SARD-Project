#!/usr/bin/env python
# A basic example of listening to a streaming API and publishing to a Kafka topic
import os
import yaml
import json
from birdy.twitter import StreamClient
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

# Configuration
keywordsfile = "keywords.txt" # one line per keyword
tokenfile = os.path.expanduser("~") + "/.twitterapi/default.yml" # twitter credentials
kafkanodes = 'xd-kafka01:9092, xd-kafka02:9092, xd-kafka03:9092, xd-kafka04:9092'

with open(keywordsfile) as f:
    keywords = f.read().splitlines()
keywords_string = ','.join(set(keywords))
 
client = KafkaClient(kafkanodes)
producer = SimpleProducer(client)

tokens = yaml.safe_load(open(tokenfile))
client = StreamClient(tokens['consumer_key'],tokens['consumer_secret'],tokens['access_token'],tokens['access_secret'])
resource = client.stream.statuses.filter.post(track=keywords_string)

for data in resource.stream():
  tweet = json.dumps(data) + '\n'
  producer.send_messages('test', tweet)
