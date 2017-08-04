from flask_sqlalchemy import SQLAlchemy

from puppies import app


# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:/puppy'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Puppy'

db = SQLAlchemy(app)