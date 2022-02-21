# importing Flask and other modules
from flask import Flask, request, render_template
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO


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
			return render_template("login.html") + "<h1> login failed</h1>"
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
	
	loginVO = LoginVO()
	loginDAO = LoginDAO()


	loginVO.firstname = firstname 
	loginVO.lastname = lastname
	loginVO.email = email
	loginVO.password = password
	loginVO.gender = gender
	loginVO.category = category

	lst = loginDAO.validateUser(loginVO)
	lst = [i.as_dict for i in lst]
	if len(lst) == 0:

		loginDAO.insertLogin(loginVO)
		return render_template("login.html")
	else:
		return render_template("signup.html") + "<h1> user already exists</h1>"
	
	return render_template("login.html")


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
	return render_template("login.html")
