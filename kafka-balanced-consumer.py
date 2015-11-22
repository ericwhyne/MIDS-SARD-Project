#!/usr/bin/python
# starting multiple copies of this will process non-overlapping segments of a topic
# note: each daemon will get a subset of topic partitions, so the topic must have more partitions than consumers
# note: the segment and offset is determined by consumer_group name, you pick this.
from pykafka import KafkaClient
import json
client = KafkaClient(
  hosts="xd-kafka01:9092, xd-kafka02:9092, xd-kafka03:9092, xd-kafka04:9092")
topic = client.topics['twitter']
balanced_consumer = topic.get_balanced_consumer(
  consumer_group='my-consumer-group',
  auto_commit_enable=True,
  zookeeper_connect='xd-zk01:2181,xd-zk02:2181,xd-zk03:2181/xdata',
  reset_offset_on_start=True
)
for message in balanced_consumer:
  if message is not None:
    data = json.loads(message.value)
    print json.dumps(data)
