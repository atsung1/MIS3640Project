import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER ='C:/Users/atsung1/Documents/Software Design/MIS3640Project/submissions'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "Some secret string here"

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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('confirmation', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    # return render_template('matchpage.html')

        #f = request.files['the_file']
        # file.save('/var/www/uploads/uploaded_file.txt')
        # return render_template('matchpage.html')
#users will upload photos on this page
#will send file back to python and return grid of colors r1 g1 b1 r2 g2 b2 ......


@app.route('/confirmation/')
def confirmation():
    #this page will display a color grid, and users will select which color
    return render_template('confirmation.html')

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
