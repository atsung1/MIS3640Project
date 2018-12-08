import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, make_response
from werkzeug.utils import secure_filename
from finalproject import getRGB_image, getDistance, getMatches, loadData
from PIL import Image
import math
import random
import csv

app = Flask(__name__)

UPLOAD_FOLDER ='static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_UPDATES = set(['csv', 'xls'])


app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# app.config["CACHE_TYPE"] = "null"

app.secret_key = "tea"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_update(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_UPDATES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matchpage', methods=['GET', 'POST'])
def matchpage():
    #this is the page for users to upload photos in order to get a color match
    if request.method == 'POST':
        #check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, request again
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        #if valid file, save the file and go to confirmation page
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'userphoto.jpg'))
            return redirect(url_for('confirmation', filename='userphoto.jpg'))
    return render_template('matchpage.html')

@app.route('/confirmation/<filename>', methods=['POST','GET'])
def confirmation(filename):
    #this page will display a color grid, and users will select which color
    #creating color grid
    rgblist = getRGB_image('static/'+filename)
    new_rgblist = []
    #convert rgb list to int
    for i in range(len(rgblist)):
        new_item = []
        for j in range(3):
            new_item.append(int(rgblist[i][j]))
        new_rgblist.append(new_item)  
    #creating separate rgb lists so we can put these values into the html page
    r, g, b = [], [], []
    for i in range(25):
            r.append(new_rgblist[i][0])
            g.append(new_rgblist[i][1])
            b.append(new_rgblist[i][2])
    if request.method == 'POST':
        #taking user input in confirmation and converting it to matches to display on results page
        colornum = int(request.form['numbers'])
        if colornum:
        #colornum needs to reference the rgb list
            colorrgb = [r[colornum-1], g[colornum-1], b[colornum-1]]
            matches = getMatches(colorrgb, 'Book1.csv')
            return render_template('results.html', colornum=colornum, colorrgb=colorrgb, matches=matches, filename=filename)
    return render_template("confirmation.html", r=r, g=g, b=b, filename=filename)

@app.route('/updatepage/', methods=['POST','GET'])
def updatepage():
    #allows users to upload csv and database to be updated
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_update(file.filename):
            a = loadData(file.filename)
            return render_template('success.html')
    return render_template('updatepage.html')

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

# if __name__ == '__main__':
#     app.run()