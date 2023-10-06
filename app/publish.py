import json
import os
import uuid
from confluent_kafka import Producer

_APP_NAME = os.environ["APP_NAME"]
_TOPIC_NAME = os.environ["KAFKA_TOPIC_NAME"]
_KAFKA_BOOTSTRAP_BROKERS = os.environ["KAFKA_BOOTSTRAP_BROKERS"]
_CONFIG = {'bootstrap.servers': _KAFKA_BOOTSTRAP_BROKERS, 'client.id': _APP_NAME}
_KAFKA_PRODUCER = Producer(_CONFIG)

"""
Test from VS-Code:
  - ensure that the kafka broker has been start from the Confluent Platform image
    (this exposes the network)
  - start a terminal window from vscode
  - start python and specify topic/broker as environment variables:
    APP_NAME=Orders KAFKA_TOPIC_NAME=test KAFKA_BOOTSTRAP_BROKERS=broker:29092 python
  - import this file and setup a payload. Publish, by executing the following
    code block:

import app.publish
payload={"aap":1,"noot":2}
app.publish.publish_event('42',payload)
"""


def publish_event(json_msg, key=None):
    if key is None:
        key = str(uuid.uuid1())
    _KAFKA_PRODUCER.produce(_TOPIC_NAME, key=key, value=json.dumps(json_msg))
