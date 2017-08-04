from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

from views import *

if __name__ == "__main__":
    with app.app_context():
        print app.name
    app.run()
