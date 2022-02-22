from project import db

class SignUpVO(db.Model):
	__tablename__ = "SignUp"
	Id = db.Column('Id', db.Integer, primary_key = True, autoincrement = True)
	firstname = db.Column('firstname', db.String(30), nullable = False)
	lastname = db.Column('lastname', db.String(30), nullable = False)
	email = db.Column('email', db.String(length=100), nullable = False, unique=True)
	password = db.Column('password', db.String(length=60),nullable = False)
	gender = db.Column('gender', db.String(20), nullable = False)
	category = db.Column('category', db.String(20), nullable = False)

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