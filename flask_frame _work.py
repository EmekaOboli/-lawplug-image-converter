from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World!'

  
@app.route("/about/")
def about():
    print('this the about page')
    return render_template('index.html')


app.run(debug = False, use_reloader = True, port = 80)
