# importing Flask and other modules
from flask import Flask, request, render_template, session, url_for, redirect
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO


from project import app


# Flask constructor

# A decorator used to tell the application
# which URL is associated function

@app.route('/', methods=["GET", "POST"])
def userLogin():
    try:
        return render_template("login.html", title = "Login")
    except Exception as ex:
        print(ex)


@app.route('/login', methods=["GET", "POST"])
def login():
    if not userLoginSession():
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
                return render_template("login.html", msg="Login Failed!", title = "Login")
            else:
                session['login_Id'] = loginVO.loginId
                session['login_email'] = loginVO.email
                return redirect(url_for('loadDashboard'))

        return render_template("login.html")
    else:
        return redirect(url_for('loadDashboard'))

@app.route('/loadDashboard', methods=["GET", "POST"])
def loadDashboard():
    if userLoginSession():
        return render_template("dashboard.html", email=session['login_email'])
    else:
        return redirect(url_for('userLogin'))


@app.route('/userLoginSession')
def userLoginSession():
    try:
        if 'login_Id' and 'login_email' in session:
            return True
        else:
            return False
    except Exception as ex:
        print(ex)


@app.route("/userLogoutSession", methods=['GET'])
def userLogoutSession():
    try:
        session.clear()
        return redirect(url_for('userLogin'))
    except Exception as ex:
        print(ex)

# @app.route('/signup', methods=["GET"])
# def userSignup():
#     try:
#         return render_template("signup.html")
#     except Exception as ex:
#         print(ex)
#
#
# @app.route('/insertUser', methods=["GET", "POST"])
# def signup():
#     # getting input with name = lname in HTML form
#     firstname = request.form['firstname']
#     # getting input with name = lname in HTML form
#     lastname = request.form['lastname']
#     # getting input with name = fname in HTML form
#     email = request.form['email']
#     # getting input with name = lname in HTML form
#     password = request.form['password']
#     # getting input with name = lname in HTML form
#     gender = request.form['gender']
#     # getting input with name = lname in HTML form
#     category = request.form['category']
#
#     loginVO = LoginVO()
#     loginDAO = LoginDAO()
#     loginVO.email = email
#     loginVO.password = password
#
#     # loginDAO.insertLogin(loginVO)
#     print("LoginVO inserted")
#
#     signupVO = SignUpVO()
#     signupDAO = SignUpDAO()
#
#     signupVO.firstname = firstname
#     signupVO.lastname = lastname
#     signupVO.gender = gender
#     signupVO.category = category
#
#     print(signupVO.signup_LoginId)
#
#
#     lst = loginDAO.validateUser(loginVO)
#
#     lst = [i.as_dict for i in lst]
#     if len(lst) == 0:
#         loginDAO.insertLogin(loginVO)
#         signupVO.signup_LoginId = loginVO.loginId
#         signupDAO.insertUser(signupVO)
#         return render_template("login.html")
#     else:
#         return render_template("signup.html", msg="User already exists!")


@app.route('/forgotPassword', methods=["GET"])
def forgotPassword():
    try:
        return render_template("forgot_password.html", title = "Forgot Password")
    except Exception as ex:
        print(ex)

@app.route('/dashboard', methods=["GET"])
def dashboard():
    try:
        return render_template("Dashboard.html", title="Dashboard")
    except Exception as ex:
        print(ex)

@app.route('/AboutUs', methods=["GET"])
def AboutUs():
    try:
        return render_template("AboutUs.html", title="About Us")
    except Exception as ex:
        print(ex)


@app.route('/updatePassword', methods=["GET", "POST"])
def updatePassword():

    # getting input with name = fname in HTML form
    email = request.form['email']
    # getting input with name = lname in HTML form
    password = request.form['confirmpswd']
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = email
    lst = loginDAO.validateUser(loginVO)
    lst = [i.as_dict for i in lst]
    if len(lst) == 0:

        return render_template("forgot_password.html",msg = "Please enter valid username.", title = "Forgot Password")
    else:
        print("___________INSIDE ELSE updatePassword_________")
        loginVO.password = password
        loginDAO.updatePassword(loginVO)
        return render_template("login.html", msg1 = "Password updated successfully.")
