from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', arg="passed")

@app.route('/result')
def data_submitted():
    return render_template('data.html', submitted_data=request.args['input_string'])