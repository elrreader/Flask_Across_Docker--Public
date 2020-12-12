from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import json
import os.path
from flask import flash
from werkzeug.utils import secure_filename
from flask import abort

app = Flask(__name__)
app.secret_key="password"

@app.route('/')
def home():
    return render_template('home.html', arg="passed")

@app.route('/result', methods=['GET', 'POST'])
def data_submitted():
    if request.method == 'POST':
        # This is for writing to a JSON file; it's used as an example of writing to a file more generally
        save_data = {}
        if os.path.exists('save_user_input_data.json'):
            
            # This is the method for checking for duplication in keys and rejecting new values with a warning to the user
            with open('save_user_input_data.json') as DataFile:
                data = json.load(DataFile)
        if request.form['input_number'] in data.keys():
            flash("Flashed message because of duplicate key")
            return redirect(url_for('home'))

        saved_user_file = request.files['file_upload']
        saved_user_file_name = secure_filename(saved_user_file.filename)
        saved_user_file.save(f'static/user_uploads/{saved_user_file_name}')

        save_data[request.form['input_number']] = request.form['input_string']
        with open('save_user_input_data.json', 'w') as DataFile:
            json.dump(save_data, DataFile)
        return render_template('data.html', transfer=save_data)
    else:
        return redirect(url_for('home'))

@app.route('/<string:static_file>')
def serve_static_file(static_file):
    if static_file == "README.md": # Actually should be looking through wherever the data for the variable URL routes might be
        return redirect(url_for('static', filename=f'user_uploads/{static_file}'))
    else:
        return abort(404)

@app.errorhandler(404)
def http_404_error(error):
    return render_template('page_not_found.html'), 404