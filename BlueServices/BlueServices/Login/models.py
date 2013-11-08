from mongoengine import *

class login(Document):
    userName = StringField()
    password = StringField()
