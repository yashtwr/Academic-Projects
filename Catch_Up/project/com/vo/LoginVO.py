from project import db

class LoginVO(db.Model):
	__tablename__ = "loginmaster"
	Id = db.Column('Id', db.Integer, primary_key = True, autoincrement = True)
	userId = db.Column('userId', db.String(100))
	password = db.Column('password', db.String(100))

	def as_dict(self):
		return{
			'Id': self.Id,
			'userId': self.userId,
			'password': self.password
		}

db.create_all()
