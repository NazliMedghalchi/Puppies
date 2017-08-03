from requests import api
from sqlalchemy import Column, INTEGER, VARCHAR, DATETIME
from puppies import db


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
        return '< User %r> ' % (self.name, self.email)

    def get(self, name, email):
        for usr in self.user:
            if usr['name'] == id and usr['email'] == email:
                return usr
        api.abort(404, "User {} doesn't exist".format(name, email))

    def create(self, name, email, password):

        self.id += 1
        self.name = name
        self.email = email
        self.password = password

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        usr = self.get(id)
        self.user.remove(usr)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode(50), unique=True)
    pic_address = db.Column('pic_address', db.Unicode(50), unique=True)
    latitude = db.Column('latitude', db.Unicode(50))
    longitude = db.Column('longitude', db.Unicode(50))
    date_time = db.Column('date_time', db.Unicode(70))

    def __init__(self, like, commenet):
        self.like += 1
        self.comment += 1

    def __repr__(self):
        return '< Post %r>' % {self.like, self.comment}
