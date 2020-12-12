from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/') # This defines the route off the domain
def home(): # This is the function that executes when the browser goes to the route above
    return render_template('home.html', arg="passed")

@app.route('/about')
def about():
    return "about page"