# importing Flask and other modules
from flask import Flask, request, render_template
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SignUpVO import SignUpVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.SignUpDAO import SignUpDAO


from project import app
# Flask constructor

# A decorator used to tell the application
# which URL is associated function

@app.route('/')
def userLogin():
    try:
        return render_template("login.html")
    except Exception as ex:
        print(ex)


@app.route('/login', methods =["GET", "POST"])
def login():
	if request.method == "POST":
		# getting input with name = fname in HTML form
		email = request.form['email']
		# getting input with name = lname in HTML form
		password = request.form['password']

		loginVO = LoginVO()
		loginDAO = LoginDAO()

		loginVO.email = email
		loginVO.password = password

		lst = loginDAO.validateLogin(loginVO)
		lst = [i.as_dict for i in lst]
		if len(lst) == 0:
			return render_template("login.html", msg = "Login Failed!")
		else:
			return render_template("dashboard.html", email = email) 
	return render_template("login.html")

@app.route('/signup', methods =["GET"])
def userSignup():
    try:
        return render_template("signup.html")
    except Exception as ex:
        print(ex)

@app.route('/insertUser', methods =["GET", "POST"])
def signup():

	# getting input with name = lname in HTML form
	firstname = request.form['firstname']
	# getting input with name = lname in HTML form
	lastname = request.form['lastname']
	# getting input with name = fname in HTML form
	email = request.form['email']
	# getting input with name = lname in HTML form
	password = request.form['password']
	# getting input with name = lname in HTML form
	gender = request.form['gender']
	# getting input with name = lname in HTML form
	category = request.form['category']
	
	signupVO = SignUpVO()
	signupDAO = SignUpDAO()
	loginVO = LoginVO()
	loginDAO = LoginDAO()

	signupVO.firstname = firstname 
	signupVO.lastname = lastname
	signupVO.email = email
	signupVO.password = password
	signupVO.gender = gender
	signupVO.category = category

	loginVO.email = email
	loginVO.password = password

	lst = signupDAO.validateUser(signupVO)

	lst = [i.as_dict for i in lst]
	if len(lst) == 0:
		signupDAO.insertUser(signupVO)
		loginDAO.insertLogin(loginVO)
		return render_template("login.html")
	else:
		return render_template("signup.html", msg = "User already exists!")


@app.route('/forgotPassword', methods =["GET"])
def forgotPassword():
    try:
        return render_template("forgot_password.html")
    except Exception as ex:
        print(ex)

@app.route('/updatePassword', methods =["GET", "POST"])
def updatePassword():

	# getting input with name = fname in HTML form
	email = request.form['email']
	# getting input with name = lname in HTML form
	password = request.form['password']
	loginVO = LoginVO()
	loginDAO = LoginDAO()

	loginVO.email = email
	lst = loginDAO.validateUser(loginVO)
	lst = [i.as_dict for i in lst]

	if len(lst) == 0:
		
		return render_template("forgot_password.html") + "please enter valid user name"
	else:
		loginVO.email = email
		loginVO.password = password
		loginDAO.updatePassword(loginVO)
		return render_template("login.html") + "<h1> password updated successfully.</h1>"
