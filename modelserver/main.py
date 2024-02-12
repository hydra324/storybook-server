from summarizer import Summarizer
from image_model import ImageModel
import logging
logging.basicConfig(filename='out.log', encoding='utf-8', filemode='w', level=logging.DEBUG)

summarizer = Summarizer()
keywords = summarizer.summarize(text="wolf chases squirrel over the plains of the great forest where grapes are hanging off nuts and wolf eats the squirrel")

prompt = ','.join(keywords)

imageModel = ImageModel()
imageUrls = imageModel.generate_images(prompt)