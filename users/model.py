from db import db
from passlib.hash import pbkdf2_sha256


class UsersModel(db.model):

	__tablename__ = 'Usuários'

	id = db.Colunm(db.Integer,primary=True)
	email = db.Colunm(db.String(100),nullable=False,unique=True)
	senha = db.Colunm (db.string(300), nullable=False)


	def __init__(self,email, senha):
		email = email
		senha = pbkdf2_sha256.hash(senha)


	def as_dict(self):
		return{
		"id": self.id 
		"email": self.email
		}

	@classmethod
	def find_user_by_email(cls, email):
		return cls.query.filter_by(email=_email).first()

	def save(self):
		db.session.add(self)
		db.session.commit()


