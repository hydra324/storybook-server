from fastapi import FastAPI
from fastapi import __version__ as fastapi_version
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
]


class ImageRequest(BaseModel):
    rawText: str

# Logging
import logging
logging.basicConfig(filename='out.log', encoding='utf-8', filemode='w', level=logging.DEBUG)

from modelserver.summarizer import Summarizer
from modelserver.image_model import ImageModel
# Load Summarizer and Image Models into VRAM
summarizer = Summarizer()
imageModel = ImageModel()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World","fastapi version":fastapi_version}

@app.post("/generate_images")
def get_images(image_request: ImageRequest):
    # TODO: push message to message queue
    keywords = summarizer.summarize(text=image_request.rawText)
    prompt = ','.join(keywords)
    imageUrls = imageModel.generate_images(prompt)
    return {"imageUrls":imageUrls}