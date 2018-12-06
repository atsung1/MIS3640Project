import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from finalproject import getRGB_image
from PIL import Image
import math
import random
import csv

app = Flask(__name__)

UPLOAD_FOLDER ='submissions'
CONFIRM_FOLDER = 'confirmationimages'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONFIRM_FOLDER'] = CONFIRM_FOLDER


app.secret_key = "tea"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matchpage', methods=['GET', 'POST'])
def matchpage():
    if request.method == 'POST':
        #check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'userphoto.jpg'))
            return redirect(url_for('confirmation', filename='userphoto.jpg'))
    #I basically can't figure out how to link it to matchpage so i made the Match page here below
    return '''
    <!doctype html>
    <head>
        <title>Match Page</title>
    </head>
    <body>
        <h1>Match Page</h1>

        <a>Upload a photo of your skin that you would like The Genie to find a match for!</a><p>

        <a>Select image to upload:</a><br>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=file>
            <input type=submit value=Upload>
        </form>
    </body>
    '''
        #f = request.files['the_file']
        # file.save('/var/www/uploads/uploaded_file.txt')
        # return render_template('matchpage.html')
        #users will upload photos on this page
        #will send file back to python and return grid of colors r1 g1 b1 r2 g2 b2 ......

# @app.route('/loading/')
# def loading():
# #this page will display loading stuff
#     # photopath = os.path.abspath()
#     rgblist = getRGB_image('submissions/userphoto.jpg')
#     new_rgblist = []
#     for i in range(len(rgblist)):
#         new_item = []
#         for j in range(3):
#             new_item.append(int(rgblist[i][j]))
#         new_rgblist.append(new_item)
#     #list of rgbs for each rectangle
#     # os.chdir('C:/Users/atsung1/Documents/Software Design/MIS3640Project/confirmationimages')
#     #establish working directory
#     for i in range(len(new_rgblist)):
#         img = Image.new('RGB', (50,50), color=tuple(new_rgblist[i]))
#         nametitle = str(i+1)
#         img.save(os.path.join(app.config['CONFIRM_FOLDER'], nametitle+'.jpg'))    
#     return render_template('loading.html')


@app.route('/confirmation/<filename>')
def confirmation(filename):
    #this page will display a color grid, and users will select which color
    # file1 = os.path.join(app.config['CONFIRM_FOLDER'], '1.jpg')

    # print(file1)
    # img_file = Image.open(file1)
    # img_file.show()
    rgblist = getRGB_image('submissions/'+filename)
    new_rgblist = []
    #convert rgb list to int
    for i in range(len(rgblist)):
        new_item = []
        for j in range(3):
            new_item.append(int(rgblist[i][j]))
        new_rgblist.append(new_item)
    #save 25 images
    # for i in range(len(new_rgblist)):
    #     img = Image.new('RGB', (50,50), color=tuple(new_rgblist[i]))
    #     nametitle = str(i+1)
    #     img.save(os.path.join(app.config['CONFIRM_FOLDER'], nametitle+'.jpg'))    
    return render_template("confirmation.html")

# @app.route('/confirmation/<path:filename>')
# def returnpic(filename):
#     return send_from_directory(app.config['CONFIRM_FOLDER'], filename)

#send the selection to python, pick appropriate RGB, calculate top 3 results
@app.route('/results/')
def results():
    #we will return top 3 results with color grid and product name
    return render_template('results.html')

@app.route('/updatepage/')
def updatepage():
    #allows database to be updated
    return render_template('updatepage.html')




# if __name__ == '__main__':
#     app.run()
