import time
from flask import Flask, request


def run(app: Flask, selectedPath: str, route: object,
        request: request, sessionId: str):
    time.sleep(float(route["sleep"]["duration"]))
