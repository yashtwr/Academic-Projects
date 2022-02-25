# importing Flask and other modules
from flask import Flask, request, render_template
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO


from project import app


# Flask constructor

# A decorator used to tell the application
# which URL is associated function

@app.route('/', methods=["GET", "POST"])
def userLogin():
    try:
        return render_template("login.html")
    except Exception as ex:
        print(ex)


@app.route('/login', methods=["GET", "POST"])
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
            return render_template("login.html", msg="Login Failed!")
        else:
            return render_template("dashboard.html", email=email)
    return render_template("login.html")


@app.route('/forgotPassword', methods=["GET"])
def forgotPassword():
    try:
        return render_template("forgot_password.html")
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

        return render_template("forgot_password.html",msg = "please enter valid Email Id")
    else:
        loginVO.password = password
        loginDAO.updatePassword(loginVO)
        return render_template("login.html", msg1 = "password updated successfully")
