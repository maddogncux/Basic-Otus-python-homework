#Launch docker container : sudo docker run  -p 88:8000 - it webappp

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hellow World!"}


@app.get("/ping/")
def ping():
    return {"message": "pong"}