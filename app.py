import logging
import time

from fastapi import FastAPI
from model import mult_item
from Multiply import mult

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI(debug=True)


@app.get("/")
def home():
    return "Hello World!"


@app.get("/health")
def health_check():
    return "OK"


@app.get("/sqrt/{value_1}/{value_2}")
def func(value_1: int, value_2: int):
    start = time.time()
    logger.info(f"Info Recieved {value_1} & {value_2}")
    logger.debug(f"Debug Recieved {value_1} & {value_2}")
    output = mult(value_1, value_2)
    end = time.time()

    logger.info(f"time = {end - start} seconds")
    return output
