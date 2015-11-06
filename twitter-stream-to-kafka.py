#!/usr/bin/python
# coding=utf-8
import yaml
import os
#from birdy.twitter import StreamClient
import json
import re
import sys
from time import strftime
from kafka import SimpleProducer, KafkaClient

keywordsfile = sys.argv[1]
tokenfile = os.path.expanduser("~") + "/.twitterapi/sard.yml"


with open(keywordsfile) as f:
    keywords = f.read().splitlines()
keywords_string = ','.join(set(keywords))

print "Tracking tweets with these keywords:", keywords_string
'''
# Connect to Twitter
tokens = yaml.safe_load(open(tokenfile))
client = StreamClient(tokens['consumer_key'],tokens['consumer_secret'],tokens['access_token'],tokens['access_secret'])
resource = client.stream.statuses.filter.post(track=keywords_string)
'''

# Configure Kafka
kafka_topic = 'twitter-stream'
kafka_hosts = "xd-kafka01:9092,xd-kafka02:9092,xd-kafka03:9092,xd-kafka04:9092"
zookeeper_hosts = 'xd-zk01:2181,xd-zk02:2181,xd-zk03:2181/xdata'

# To send messages synchronously
kafka = KafkaClient(kafka_hosts)
producer = SimpleProducer(kafka)
producer.send_messages(b'test-topic', u'你怎么样?'.encode('utf-8'))

#print client.topics
'''
for data in resource.stream():
   tweetlog.write(json.dumps(data) + '\n')
   if 'text' in data:
       print data['text']
'''
