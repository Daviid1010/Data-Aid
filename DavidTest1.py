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



###### Refactoring for Database Entry (not dynamic yet!!!)
InvoiceNum = arrays[5]
shop = arrays[0]
print(shop)
shopAddress1 = arrays[1]
shopAddress2 = arrays[2]
print("Shop Address 1: ",shopAddress1)
print("Shop Address 2: ",shopAddress2)

print("VAT Number:",data[6][-8:])
InvoiceNum = data[6][-8:]

date = datetime.date(datetime.now())
dateStr = date.strftime("%d/%m/%Y")
print(dateStr)

item1 = arrays[5]
print("Item 1: "+item1)
split1 = item1.split("\n");
print(split1)
line1desc = split1[0]
line1price = split1[6]
line1quantity = 1


print("####### Item 1")
print(line1desc)
print(line1price)
print(line1quantity)



item2 = arrays[6]
print("Item 2: "+item2)
split2 = item2.split("\n")
print(split2)
line2desc = split2[1]
line2price = split2[4][-5:]
quantityline2 = 1

print("###### Item 2")
print(line2desc)
print(line2price)
print(quantityline2)





item3 = arrays[7]
print("Item 3: "+item3)
split3 = item3.split("\n")
print(split3)
item3desc = split3[0]


split4 = arrays[8]
print(split4)
item3price = split4[-4:]
item3quantity = 1

print("############ Item 3 ")
print(item3desc)
print(item3price)
print(item3quantity)

