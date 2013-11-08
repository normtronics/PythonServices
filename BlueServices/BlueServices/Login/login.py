from mongoengine import *
connect('user', host='mongodb://cnorman:pernell1@ds031088.mongolab.com:31088/MongoLab-2')



class login:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def validate(name, password):
        if name ==  null :
            return 'yo'

    def checkIfInSystem(name):
        return null
   


