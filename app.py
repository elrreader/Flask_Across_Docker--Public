from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', arg="passed")

@app.route('/result', methods=['GET', 'POST'])
def data_submitted():
    if request.method == 'POST':
        # This is for writing to a JSON file; it's used as an example of writing to a file more generally
        save_data = {}
        save_data[request.form['input_number']] = request.form['input_string']
        with open('save_user_input_data.json', 'a') as DataFile:
            json.dump(save_data, DataFile)
        return render_template('data.html', transfer=save_data)
    else:
        return redirect(url_for('home'))