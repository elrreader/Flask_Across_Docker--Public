from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', arg="passed")

@app.route('/result', methods=['GET', 'POST'])
def data_submitted():
    if request.method == 'POST':
        return render_template('data.html', submitted_data=request.form['input_string'])
    else:
        return redirect(url_for('home'))