import os, datetime, geocoder, requests
import uuid

from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, json
from flask import session, g, redirect, url_for, abort, flash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1:5000/puppy'
db = SQLAlchemy(app)
api = Api(app)

# urlvars = False  # Build query strings in URLs
# swagger = True  # Export Swagger specifications


# def get_db():
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = sqlite3.connect('Puppy')
#     return g.sqlite_db
#

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# conn = mysql.connect()
@app.route("/")
def main():
    return render_template('index.html')


# show just signup page - not functioning
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


# create signup function
# create user code will be here !!
@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']


    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column('id', db.Integer, primary_key=True)
        name = db.Column('name', db.Unicode(50), unique=True)
        email = db.Column('email', db.Unicode(50), unique=True)
        password = db.Column('password', db.Unicode(50))
        authentication_key = db.Column('authentication_key', db.String(70), unique=True)

        # insert data to table
        def __init__(self, name, email):
            self.name = name
            self.email = email

        def __repr__(self):
            return '< User %r> ' % {self.name, self.email}

    # validate the received values
    if name and email and password:

        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/upload', methods=['GET','POST'])
def postPic():

    if requests.method == 'POST':
        file = requests.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        jLoad = json.loads(r.text)
        latitude = jLoad['latitude']
        longitude = jLoad['longitude']
        title = request.form('title')
        date_time = datetime.datetime.now()
        address_pic = request.form('file_name')

    class Post(db.Model):
        __tablename__ = 'post'
        id = db.Column('id', db.Integer, primary_key=True)
        title = db.Column('title', db.Unicode(50), unique=True)
        pic_address = db.Column('pic_address', db.Unicode(50), unique=True)
        like = db.Column('like', db.Integer(100))
        comment = db.Column('comment', db.Integer(100))
        latitude = db.Column('latitude', db.Unicode(50))
        longitude = db.Column('longitude', db.Unicode(50))
        date_time = db.Column('date_time', db.Unicode(70))

        def __init__(self, like, commenet):
            self.like += 1
            self.comment += 1

        def __repr__(self):
            return '< Post %r>' % {self.like, self.comment}


if __name__ == "__main__":
    app.run()
