import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from finalproject import getRGB_image, getDistance, getMatches, loadData
from PIL import Image
import math
import random
import csv

app = Flask(__name__)

UPLOAD_FOLDER ='static'
CONFIRM_FOLDER = 'confirmationimages'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
CSV_FOLDER = 'csvfolder'


app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONFIRM_FOLDER'] = CONFIRM_FOLDER
app.config['CSV_FOLDER'] = CSV_FOLDER


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


@app.route('/confirmation/<filename>', methods=['POST','GET'])
def confirmation(filename):
    #this page will display a color grid, and users will select which color
    # file1 = os.path.join(app.config['CONFIRM_FOLDER'], '1.jpg')

    # print(file1)
    # img_file = Image.open(file1)
    # img_file.show()
    rgblist = getRGB_image('static/'+filename)
    new_rgblist = []
    #convert rgb list to int
    for i in range(len(rgblist)):
        new_item = []
        for j in range(3):
            new_item.append(int(rgblist[i][j]))
        new_rgblist.append(new_item)
    #build 3 lists
    # for i in range(len(new_rgblist)):
    #     img = Image.new('RGB', (50,50), color=tuple(new_rgblist[i]))
    #     nametitle = str(i+1)
    #     img.save(os.path.join(app.config['CONFIRM_FOLDER'], nametitle+'.jpg'))    
    #save 25 images
    # for i in range(len(new_rgblist)):
    #     img = Image.new('RGB', (50,50), color=tuple(new_rgblist[i]))
    #     nametitle = str(i+1)
    #     img.save(os.path.join(app.config['CONFIRM_FOLDER'], nametitle+'.jpg'))    
    r = []
    g = []
    b = []
    for i in range(25):
            r.append(new_rgblist[i][0])
            g.append(new_rgblist[i][1])
            b.append(new_rgblist[i][2])

    if request.method == 'POST':
        #everything in here is when users input
        colornum = int(request.form['numbers'])
        # a = float(request.form['a'])
        # b = float(request.form['b'])
        # c = float(request.form['c'])
        # root_1, root_2 = quadratic(a, b, c)
        # print(colornum) #check if input is working
        if colornum:
        #colornum needs to reference the rgb list
            colorrgb = [r[colornum-1], g[colornum-1], b[colornum-1]]
            # somelist = loadData(os.path.join(app.config['CSV_FOLDER']+'/Shiseido_products.csv'))            
            matches = getMatches(colorrgb, os.path.join(app.config['CSV_FOLDER']+'/Shiseido_products.csv'))
            print(matches)
            return render_template('results.html', colornum=colornum)

    return render_template("confirmation.html", r1=r[0], r2=r[1], r3=r[2], r4=r[3], r5=r[4], r6=r[5], r7=r[6], r8=r[7],
                           r9=r[8],r10=r[9],r11 = r[10],r12 = r[11],r13=r[12],r14=r[13],r15 = r[14],r16 = r[15],
                           r17=r[16],r18 = r[17],r19 = r[18],r20 = r[19],r21 = r[20],r22 = r[21],r23 = r[22],r24 = r[23]
                           ,r25 = r[24],g1=g[0], g2=g[1], g3=g[2], g4=g[3], g5=g[4], g6=g[5], g7=g[6], g8=g[7], g9=g[8],
                           g10=g[9],g11 = g[10],g12 = g[11],g13=g[12],g14=g[13],g15 = g[14],g16 = g[15],g17=g[16],
                           g18 = g[17],g19 = g[18],g20 = g[19],g21 = g[20],g22 = g[21],g23 = g[22],g24 = g[23],
                           g25 = g[24], b1=b[0], b2=b[1], b3=b[2], b4=b[3], b5=b[4], b6=b[5], b7=b[6], b8=b[7], b9=b[8],
                           b10=b[9],b11 = b[10],b12 = b[11],b13=b[12],b14=b[13],b15 = b[14],b16 = b[15],b17=b[16],
                           b18 = b[17],b19 = b[18],b20 = b[19],b21 = b[20],b22 = b[21],
                           b23 = b[22],b24 = b[23],b25 = b[24])

# @app.route('/confirmation/<path:filename>')
# def returnpic(filename):
#     return send_from_directory(app.config['CONFIRM_FOLDER'], filename)

#send the selection to python, pick appropriate RGB, calculate top 3 results
# @app.route('/results/', methods=['GET', 'POST'])
# def results():
    #we will return top 3 results with color grid and product name
    # if request.method == 'POST':
    #     r = request.form['numbers']
    #     print(r)
        # matches = getMatches()
    # return render_template('results.html')

@app.route('/updatepage/')
def updatepage():
    #allows database to be updated
    return render_template('updatepage.html')




# if __name__ == '__main__':
#     app.run()
