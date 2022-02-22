from project import db

class LoginVO(db.Model):
	__tablename__ = "loginmaster"
	Id = db.Column('Id', db.Integer, primary_key = True, autoincrement = True)
	email = db.Column('email', db.String(length=100), nullable = False, unique=True)
	password = db.Column('password', db.String(length=60),nullable = False)

	def as_dict(self):
		return{
			'Id': self.Id,
			'userId': self.email,
			'password': self.password
		}

db.create_all()
