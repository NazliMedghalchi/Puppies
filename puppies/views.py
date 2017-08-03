import datetime
import requests

from flask import render_template
from flask import request, json, g
from puppies import app



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


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    # validate the received values
    if name and email and password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/upload', methods=['POST'])
def postPic():
    file = requests.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid.uuid4()) + extension
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    jLoad = json.loads(r.text)

    title = request.form('title')
    address_pic = request.form('file_name')
    latitude = jLoad['latitude']
    longitude = jLoad['longitude']
    date_time = datetime.datetime.now()


@app.route('/showAll', methods=['GET'])
def showPuppy():
    return
