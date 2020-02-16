import cv2
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

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
print(data)
arrays.remove(" ")
arrays.remove("  ")
print(arrays)



###### Refactoring for Database Entry (not dynamic yet!!!)
shop = arrays[0]
print(shop)
shopAddress1 = arrays[1]
shopAddress2 = arrays[2]
print(shopAddress1)
print(shopAddress2)


item1 = arrays[5]
print("Item 1: "+item1)
item2 = arrays[6]
print("Item 2: "+item2)
item3 = arrays[7]
print("Item 3: "+item3)

