import cv2
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

import pandas as pd
from datetime import datetime
import os

##print(os.getcwd())

############################
### Pre-Processing Here


out = pytesseract.image_to_string(cv2.imread("Images/schuh.jpeg"))


####P Print Out of Raw Text
print(out)


#### Split Data into Arrays
arrays = out.split("\n\n")
data = out.split("\n")
print("Data: ",data)
arrays.remove(" ")
arrays.remove("  ")
print("Arrays: ",arrays)
splitArrays = arrays