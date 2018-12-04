from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/csvpage/')
def csvpage():
    return render_template('csvpage.html')

@app.route('/matchpage/')
def matchpage():
    return render_template('matchpage.html')

@app.route('/confirmation/')
def confirmation():
    return render_template('confirmation.html')

@app.route('/results/')
def results():
    return render_template('results.html')

# if __name__ == '__main__':
#     app.run()
