import json
from fastapi import FastAPI
from fastapi import __version__ as fastapi_version

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World","fastapi version":fastapi_version}

@app.get("/")
def get_images(raw_text: str):
    # TODO: push message to message queue
    
    return {"imageUrls":["url1","url2","url3"]}