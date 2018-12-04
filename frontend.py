from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/matchpage/')
def matchpage():
    #users will upload photos on this page
    return render_template('matchpage.html')
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
