from mongoengine import *
from BlueServices import Entity
connect('user', host='mongodb://user:pass@ds031088.mongolab.com:31088/MongoLab-2')



class loginEntity():
    def __init__(self, name, password):
        self.name = name
        self.passw = password

    def checkIfInSystem() :
        for users in UserEntity :
            if users.name.userName == self.name :
                print users
                this.loggedInUser = users
                return checkIfCorrectPass(users, self.password)
            else :
                return 0

    def checkIfCorrectPass(user, password) :
        if user.password == password :
            return user
        else :
            return 0
                

        
   


