from mongoengine import *

class NameEntity(EmbeddedDocument):
	firstName = StringField(max_length = 50)
	lastName = StringField(max_length = 50)
	displayName = StringField(max_length = 50)
	userName = StringField(max_length = 50)


class AddressEntity(EmbeddedDocument):
	Street = StringField()
	City = StringField()
	State = StringField(max_length = 50)
	Zip = StringField(max_length = 5)

class UserEntity(Document):
	email = EmailField()
	password = StringField(min_length = 6)
	name = EmbeddedDocumentField(NameEntity)
	address = EmbeddedDocumentField(AddressEntity)


