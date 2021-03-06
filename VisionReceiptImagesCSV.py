import os, io
import google.cloud
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\david\Downloads\My Project 89279-337745e1ad77.json"

client = vision.ImageAnnotatorClient()

image_to_open = os.path.join(os.path.dirname(__file__),
                             'ReceiptImages/1001-receipt.jpg')




with open(image_to_open, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

text_respone = client.text_detection(image=image)
texts = text_respone.text_annotations
print('Texts: ')
for text in texts:
    print("\n {}".format(text.description))
if text_respone.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            text_respone.error.message)
    )
