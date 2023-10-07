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
import os
import publish
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from datetime import datetime
from order import Order


_APP_NAME = os.environ["APP_NAME"]

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

# TODO - add typing to perform validation for order object
@app.post("/order", status_code=201)
async def handle_order(order: Order):
    try:
        print(f"You sent in a request to {_APP_NAME}: ", order)
        try:
            order_event = publish.msg_to_event(event_name="OrderCreated", msg=order.model_dump())
            publish.publish_event(event=order_event)
            return JSONResponse({
                'status': "OK", 
                "message": "Order created",
                "event": order_event
            })
        except Exception as e:
            return JSONResponse(
                {'status': "Error while publishing message", "message": str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        return JSONResponse(
            {'status': "Error", "message": str(e)},
            status_code=status.HTTP_400_BAD_REQUEST
        )
