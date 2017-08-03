from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

from puppies import app


# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:/puppy'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'db_username_here'
app.config['MYSQL_PASSWORD'] = 'db_password_here'
app.config['MYSQL_DB'] = 'database_name_here'

db = SQLAlchemy(app)