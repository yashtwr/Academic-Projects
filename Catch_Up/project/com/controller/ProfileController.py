# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for, session
from project.com.vo.LoginVO import LoginVO
from project.com.vo.CoursesVO import CoursesVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.CoursesDAO import CoursesDAO
from project.com.vo.EducationVO import EducationVO
from project.com.dao.EducationDAO import EducationDAO


from project import app


@app.route('/profile', methods=["GET"])
def userProfile():
    try:
        return render_template("profile_setup.html", title = "profileSetup")
    except Exception as ex:
        print(ex)


@app.route('/profileSetup', methods=["GET", "POST"])
def profile():
    # getting input with course_no = course_no in HTML form
    course_no = request.form['course_no']
    # getting input with department = department in HTML form
    department = request.form['department']
    degree_name = request.form['degree_name']
    institution_name = request.form['institution_name']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    cgpa = request.form['cgpa']

    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    educationVO = EducationVO()
    educationDAO = EducationDAO()

    courseVO.course_no = course_no
    courseVO.department = department

    educationVO.degree_name = degree_name
    educationVO.institution_name = institution_name
    educationVO.start_date = start_date
    educationVO.end_date = end_date
    educationVO.cgpa = cgpa

    loginVO.email = session['login_email']

    lst = loginDAO.validateUser(loginVO)

    lst = [i.as_dict for i in lst]
    if len(lst) > 0:
        courseVO.course_loginId = loginDAO.fetchId(loginVO)
        courseDAO.insertCourses(courseVO)
        educationVO.education_loginId = loginDAO.fetchId(loginVO)
        educationDAO.insertEdu(educationVO)
        return render_template("show_profile.html", msg1 = "Profile editted successfully", title = "Profile", courses = courseVO, education = educationVO)
    else:
        return render_template("signup.html", msg="User already exists!", title = "SignUp")
