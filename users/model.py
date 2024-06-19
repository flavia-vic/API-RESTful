from db import db
from passlib.hash import pbkdf2_sha256


class UsersModel(db.Model):

	__tablename__ = 'Usuários'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(80), unique=True, nullable=False)
	senha = db.Column (db.String(120), unique=True, nullable=False)


	def __init__(self,email, senha):
		self.email = email
		self.senha = pbkdf2_sha256.hash(senha)


	def as_dict(self):
		return {
		"id": self.id, 
		"email": self.email
		}

	@classmethod
	def find_user_by_email(cls, _email):	
 		return cls.query.filter_by(email=_email).first()


	def save(self):
 		db.session.add(self)
 		db.session.commit()