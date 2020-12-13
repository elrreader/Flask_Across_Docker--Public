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
import mysql.connector as mysql
from flask_sqlalchemy import SQLAlchemy
import Private.Database_Credentials as Credentials

app = Flask(__name__)
app.secret_key="password"
# app.run(debug=TRUE)
Database='InfoIsUs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysql.connect://' + Credentials.Username + ':' + Credentials.Password + '@' + Credentials.Host + ':' + str(Credentials.Post) + '/' + Database


##################
# Connect to MySQL
def MySQL_Connection(DB):
    return mysql.connect(
        host = Credentials.Host,
        user = Credentials.Username,
        password=Credentials.Password,
        database=DB
    )

#Alert: Cursor is parameter, not established within function for non-Flask app; can also pass in connection object
def Insert_JobTitle(Title, SOC, FK_Table_Input): # Final parameter is list of tuples where each tuple is the data going into a record
    Input = (Title, SOC) #ToDo: Confirm this is creating a tuple
    # Viable value: ("Teacher", 6)
    Connection = MySQL_Connection(Database)
    Cursor = Connection.cursor()
    #ToDo: Adjust f-string to take from tuple
    Cursor.execute(f'INSERT INTO JobTitle(jobTitle, SOC) VALUES ({1}, {2});')

    PK_of_Last_Record_Inserted = Cursor.lastrowid

    Inputs = []
    for record in FK_Table_Input:
        record_inputs = (PK_of_Last_Record_Inserted, record) #ToDo: Figure out unpacking contents of tuple "record" into tuple "record_inputs"
        Inputs.append(record_inputs)
    #ToDo: Adjust f-string to take from tuple
    Cursor.executemany(f"""SQL Statement {1}, {2}""") # This executes the statement multiple times?
    Connection.commit()
    Connection.close()

def Select_JobTitle():
    Connection = MySQL_Connection(Database)
    Cursor = Connection.cursor()
    Cursor.execute('SELECT * FROM JobTitle')
    Records = Cursor.fetchall() # This returns a standard list
    print(Records)
    print(type(Records))
    Connection.close()

##################

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

@app.route('/SQL') #ToDo: Finish functionality
def Write_SQL_Query():
    return render_template('Write_SQL_Query.html')

@app.route('/database', methods=['GET', 'POST']) #ToDo: Finish functionality
def SQL_Results():
    return render_template('SQL_Results.html')

######################################
# Copy of Python and Databases Example

SQLAlchemy_DB = SQLAlchemy(app)

class OccupationClass_Table(SQLAlchemy_DB.model):
    """CREATE TABLE OccupationClass (
        occupationClassID INT NOT NULL AUTO_INCREMENT,
        SOC VARCHAR(50) NULL,
        PRIMARY KEY (occupationClassID))
  """
    __tablename__ = 'OccupationClass'

    occupationClassID = SQLAlchemy_DB.Column(SQLAlchemy_DB.Integer, primary_key=True)
    SOC = SQLAlchemy_DB.Column(SQLAlchemy_DB.String(length=50))



@app.route('/enter-data')
def Enter_Data():
    return render_template('Data_Entry_Form.html', Table=OccupationClass_Table.query.all())

@app.route('/SOC/<SOC_ID>')
def Show_SOC_and_Jobs(SOC_ID):
    return render_template('SOC_and_Jobs.html', SOC=SOC_ID)

@app.route('/add/SOC', methods=['POST']) # Will only accept POST, because GET doesn't have data the DB can add
def Add_SOC():
    #add 
    return "SOC added"

@app.route('/add/job/<SOC_ID>', methods=['POST'])
def Add_Job(SOC_ID):
    #add
    return "Job added"