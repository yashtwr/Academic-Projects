from project import db

class LoginVO(db.Model):
	__tablename__ = "loginmaster"
	Id = db.Column('Id', db.Integer, primary_key = True, autoincrement = True)
	firstname = db.Column('firstname', db.String(100))
	lastname = db.Column('lastname', db.String(100))
	email = db.Column('email', db.String(100))
	password = db.Column('password', db.String(100))
	gender = db.Column('gender', db.String(100))
	category = db.Column('category', db.String(100))

	def as_dict(self):
		return{
			'Id': self.Id,
			'firstname': self.firstname,
			'lastname': self.lastname,
			'email': self.email,
			'password': self.password,
			'gender': self.gender,
			'category': self.category
		}

db.create_all()
