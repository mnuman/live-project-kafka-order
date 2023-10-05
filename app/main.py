from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from datetime import datetime

APP_NAME = "Orders"

app = FastAPI(
    title="Order Microservice",
    description="Python Order Microservice to be dockerized",
    summary="Receive orders. Rule the world.",
    version="0.0.1",
    contact={"name": "Milco Numan", "url": "https://github.com/mnuman/live-project-kafka-order"},
)

@app.get("/health")
async def root():
    return {
        "status": "Running",
        "application": APP_NAME,
        "timestamp": datetime.now()
        }

@app.get("/")
async def redirect_typer():
    return RedirectResponse("/health")