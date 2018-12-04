from PIL import Image
import os
import math
import random
import csv

# establish working directory
os.chdir('C:/Users/jhe1/Documents/GitHub/mis3640/finalproject')
# must use a larger file

def getRGB_image(filepath):
    # gets the image pixel array from filepath
    img_file = Image.open(filepath)

    img = img_file.load()

    [xs, ys] = img_file.size
    print("The image resolution is" , xs, "*", ys)

    # get the number of samples in each rectangle, 5% of total pixels in the rectangle
    num_samples = math.ceil(ys * xs * .002)

    # establish a variable to hold the rgb's for each rectangle
    allRectangles = []

    # divide the image into 25 (5x5) equal rectangles and store in an list
    for y_split in range(5):
        # loop through each row of rectangles
        for x_split in range(5):
            # loop through each rectangle in the row
            y_min = math.ceil(ys / 5 * y_split)
            y_max = math.ceil(ys / 5 * (y_split + 1))
            x_min = math.ceil(xs / 5 * x_split)
            x_max = math.ceil(xs / 5 * (x_split + 1))

            # print(y_split * 5 + x_split + 1)
            # print(y_min, y_max)
            # print(x_min, x_max)

            # establish a list to hold the sample taken from the current rectangle
            currentRectangle = []

            # get random x and y values for points
            rect_y = random.choices(range(y_min, y_max), k=num_samples)
            rect_x = random.choices(range(x_min, x_max), k=num_samples)

            for n in range(num_samples):
                # get random values in the current rectangle and add to list
                # print(n)
                [r, g, b] = img[rect_x[n], rect_y[n]]
                currentRectangle.append([round(r), round(g), round(b)])

            # add the current rectangle to the list of all 25
            allRectangles.append([sum(color) / len(color) for color in zip(*currentRectangle)])

        # for n in range(len(allRectangles)):
        #     print(n + 1, allRectangles[n])

    return allRectangles

def getRGB_pixel(filepath):
    # pulls the RGB values of that pixel and returns a list of the RGB code
    im = Image.open(filepath)
    rgb_im = im.convert('RGB')
    output = []
    for i in rgb_im.getpixel((0, 0)):
        output.append(i)
    return output



# pulls all data from a csv, should have brand name, name of makeup color, price, size, color code
def loadData(filepath):


    raw = []
    # open a connection to the source csv
    with open(filepath) as csvfile:
        # convert the source data's rows into lists
        reader = csv.reader(csvfile, delimiter = ',')
        # make all rows into one list
        for row in reader:
            raw.append(row)
    # loop through each row and loads RGB code of each file path
    for item in raw:
        # skip items that do not have color codes
        if item[2] != "NA":
            code = getRGB_pixel(item[9])
            item.extend(code)
    # make a connection to the database csv
    with open('Book1.csv', 'w', newline='') as csvfilew:
        data_writer = csv.writer(csvfilew, delimiter=',')
        for item in raw:
            data_writer.writerow(item)
    # return the list with all information, added with RGB color code
    return raw



# calculate square root of sum of squares for R G and B values between the target and option
def getDistance(target,option):
    results = 0
    for i in [0,1,2]:
        result = (float(target[i]) - float(option[i]))**2
        results += result

    return(math.sqrt(results))

def getMatches(list, filepath):
    # calculate max distance as maxdist with getDistance (0,0,0) vs (255,255,255)
    maxdist = getDistance([0,0,0],[255,255,255])
    # load csv
    with open(filepath, 'r') as csvfile:
        # convert the source data's rows into lists
        reader = csv.reader(csvfile, delimiter = ',')

    # create a temp list for final lookup
        chart = {}
    # loop through each row of the dataframe
        for item in reader:
            # making sure it has color code
            if item[2] != 'NA':
                # load R G and B into reference list
                itemRGB = [item[10],item[11],item[12]]
                # calculate getDistance() with the target input list and reference list parameters
                dist = getDistance(list, itemRGB)
                # add to new similarity column the  decimal (1 - (calculated distance / maxdist)
                # to get % match
                match = (1-(dist/maxdist))
                # record the match % into a temp list
                chart[item[0]] = match
    # sort 3 closest
    import operator
    sorted_chart = sorted(chart.items(), key=operator.itemgetter(1))
    print(sorted_chart[0:3])

#just testing
print(loadData('Shiseido_products.csv'))
getMatches([234,206,189],'Book1.csv')