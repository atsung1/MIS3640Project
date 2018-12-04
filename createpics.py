# this is the program created to create a single-pixel picture for each of the items that have a
# color code in the list
# this will also add the file path for the corresponding picture


from PIL import Image
import os
import math
import random
import csv

# establish working directory
os.chdir('C:/Users/jhe1/Documents/GitHub/mis3640/finalproject')


# Translate the Color code to RGB (in tuple)
def RGB(colorcode):
    h = str(colorcode).lstrip('#')
    return(tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))


# load the source .csv for the information needed
def createpic(filepath):
    raw = []
    # open a connection to the source csv
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        # read all rows with color codes
        for row in reader:
            # raw.append(row)
            if row[2] != "NA":
                # convert hex code RGB tuple
                code = RGB(row[2])
                # create new image, with names of product ID
                img = Image.new('RGB', (1,1), color=code)
                productnum = row[8]
                img.save(productnum+'.png',format='PNG')
                row.append(productnum+'.png')
                raw.append(row)
            else:
                raw.append(row)

    # write the file directory to the source csv
    with open('Shiseido_products.csv', 'w', newline='') as csvfilew:
        data_writer = csv.writer(csvfilew, delimiter=',')
        for item in raw:
            data_writer.writerow(item)

createpic('Shiseido_products.csv')

# print(loadData('Shiseido_products.csv'))
#
# # r, g, and b are 512x512 float arrays with values >= 0 and < 1.
# from PIL import Image
# import numpy as np
# rgbArray = np.zeros((512,512,3), 'uint8')
# rgbArray[..., 0] = r*256
# rgbArray[..., 1] = g*256
# rgbArray[..., 2] = b*256
# img = Image.fromarray(rgbArray)
# img.save('myimg.jpeg')