"""
    Milestone 1:
    Create a new Order microservice in Go.
        Create an HTTP GET endpoint to check the microservice’s health.
        Test that the service works as expected by running the service and
        executing a call to the health endpoint. Ensure it responds accordingly.

    Milestone 2:
    Create a function that publishes an event to a topic in Kafka.
        Test that this function works correctly by creating a main program in
        Go that will use this function to publish an event to the OrderReceived topic.
        Verify that it was received by using the appropriate Kafka command-line
        operation. The easiest way to verify that an event exists in a topic is to
        use the  command illustrated in Step 5 of the “Apache Kafka Quickstart” guide.
"""
import json
import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from datetime import datetime
from confluent_kafka import Producer

_APP_NAME = "Orders"
_TOPIC_NAME = os.environ["KAFKA_TOPIC_NAME"]
_KAFKA_BOOTSTRAP_BROKERS = os.environ["KAFKA_BOOTSTRAP_BROKERS"]
_CONFIG = {'bootstrap.servers': _KAFKA_BOOTSTRAP_BROKERS, 'client.id': _APP_NAME}
_KAFKA_PRODUCER = Producer(_CONFIG)

app = FastAPI(
    title="Order Microservice",
    description="Python Order Microservice to be dockerized",
    summary="Receive orders. Rule the world.",
    version="0.0.1",
    contact={
        "name": "Milco Numan",
        "url": "https://github.com/mnuman/live-project-kafka-order"
    },
)


@app.get("/health")
async def root():
    return {
        "status": "Running",
        "application": _APP_NAME,
        "timestamp": datetime.now()
        }


@app.get("/")
async def redirect_typer():
    return RedirectResponse("/health")

"""
Test from VS-Code: 
  - ensure that the kafka broker has been start from the Confluent Platform image
    (this exposes the network)
  - start a terminal window from vscode
  - start python and specify topic/broker as environment variables:
    KAFKA_TOPIC_NAME=test KAFKA_BOOTSTRAP_BROKERS=broker:29092 python
  - import this file and setup a payload. Publish, by executing the following
    code block:

import app.main
payload={"aap":1,"noot":2}
app.main.publish_event('42',payload)
"""
def publish_event(key, json_msg):
    _KAFKA_PRODUCER.produce(_TOPIC_NAME, key=key, value=json.dumps(json_msg))
