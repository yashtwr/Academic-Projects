# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for, session
from project.com.vo.LoginVO import LoginVO
from project.com.vo.CoursesVO import CoursesVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.CoursesDAO import CoursesDAO
from project.com.vo.EducationVO import EducationVO
from project.com.dao.EducationDAO import EducationDAO
from project.com.vo.CertificatesVO import CertificatesVO
from project.com.dao.CertificatesDAO import CertificatesDAO
from project.com.vo.HobbiesVO import HobbiesVO
from project.com.dao.HobbiesDAO import HobbiesDAO
from project.com.vo.IndustryExpVO import IndustryVO
from project.com.dao.IndustryExpDAO import IndustryDAO
from project.com.vo.PersonalVO import PersonalVO
from project.com.dao.PersonalDAO import PersonalDAO
from project.com.vo.ProjectVO import ProjectVO
from project.com.dao.ProjectDAO import ProjectDAO
from project.com.vo.SkillsVO import SkillsVO
from project.com.dao.SkillsDAO import SkillsDAO
from project.com.vo.SignUpVO import SignUpVO
from project.com.dao.SignUpDAO import SignUpDAO


from project import app


@app.route('/profile', methods=["GET","POST"])
def userProfile():
    try:
        courseVO = CoursesVO()
        courseDAO = CoursesDAO()
        certificatesVO = CertificatesVO()
        certificatesDAO = CertificatesDAO()
        industryVO = IndustryVO()
        industryDAO = IndustryDAO()

        personalVO = PersonalVO()
        personalDAO = PersonalDAO()
        signupVO = SignUpVO()
        signupDAO = SignUpDAO()

        educationVO = EducationVO()
        educationDAO = EducationDAO()

        projectVO = ProjectVO()
        projectDAO = ProjectDAO()

        loginVO = LoginVO()
        loginDAO = LoginDAO()
        
        loginVO.email = session['login_email']
        id = loginDAO.fetchId(loginVO)

        courseVO.course_loginId = id
        lst = courseDAO.fetchCourses(courseVO)
        courses = [i.as_dict() for i in lst]
        
        certificatesVO.certificates_loginId = id
        lst_certi = certificatesDAO.fetchCertificates(CertificatesVO)
        certificates = [i.as_dict() for i in lst_certi]

        industryVO.industry_loginId = id
        lst_industry = industryDAO.fetchIndustryExp(industryVO)
        industryExp = [i.as_dict() for i in lst_industry]
        print(industryExp)

        personalVO.personal_loginId = id
        lst_personal = personalDAO.fetchPersonal(personalVO)
        personal = [i.as_dict() for i in lst_personal]
        print(personal)

        signupVO.signup_LoginId = id
        lst_signup = signupDAO.fetchUser(signupVO)
        signup = [i.as_dict() for i in lst_signup]
        print(signup)

        educationVO.education_loginId = id
        lst_education = educationDAO.fetchEducation(educationVO)
        education = [i.as_dict() for i in lst_education]
        print(education)

        projectVO.project_loginId = id
        lst_project = projectDAO.fetchProjects(projectVO)
        project = [i.as_dict() for i in lst_project]
        print(project)

        if 'currentPage' not in session:
            session['currentPage'] = 'personal_information'

        return render_template("profilesetup_changes.html", title = "profileSetup", courses = courses, certificates = certificates, industryExp = industryExp, signup = signup, personal = personal, education = education, projects = project)
    except Exception as ex:
        print(ex)


@app.route('/insertCourse', methods=["GET","POST"])
def insertCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    courseVO.course_no = request.form['courseno1']
    courseVO.department = request.form['department']
    # courseVO.department = request.args.get('department')
    # courseVO.department = department
    courseVO.course_loginId = loginDAO.fetchId(loginVO)

    courseDAO.insertCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))

@app.route('/updateCourse', methods=["GET","POST"])
def updateCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    course_no = request.form['course_no'+str(Id)]
    department = request.form['department']
    loginId = loginDAO.fetchId(loginVO)

    courseVO.Id = Id
    courseVO.course_no = course_no
    courseVO.department = department
    courseVO.course_loginId = loginId
    courseDAO.updateCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))

@app.route('/deleteCourse', methods=["GET"])
def deleteCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    
    loginVO.email = session['login_email']
    
    course_no = request.args.get('courseid')
    courseVO.course_no= course_no

    login_id = loginDAO.fetchId(loginVO)
    courseVO.course_loginId = login_id

    courseDAO.deleteCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))

@app.route('/insertCertificates', methods=["GET"])
def insertCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    
    loginVO.email = session['login_email']
    
    certificatesVO.certificates = request.args.get('certificates')
    
    certificatesVO.certificates_loginId = loginDAO.fetchId(loginVO)
    certificatesDAO.insertCertificates(certificatesVO)
    session['currentPage'] = 'skills'

    return redirect(url_for("userProfile"))

@app.route('/updateCertificates', methods=["GET","POST"])
def updateCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    certificates = request.form['certificate'+str(Id)]
    loginId = loginDAO.fetchId(loginVO)

    certificatesVO.Id = Id
    certificatesVO.certificates = certificates
    certificatesVO.course_loginId = loginId
    certificatesDAO.upadateCertificates(certificatesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/deleteCertificates', methods=["GET"])
def deleteCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    
    loginVO.email = session['login_email']
    Id = request.args.get('Id')
    certificatesVO.Id = Id
    certificatesVO.certificates_loginId = loginDAO.fetchId(loginVO)
    certificatesDAO.deleteCertificates(certificatesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))

@app.route('/insertIndustryExp', methods=["POST"])
def insertIndustryExp():
    industryVO = IndustryVO()
    industryDAO = IndustryDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    
    loginVO.email = session['login_email']

    industryVO.company_name = request.form['company_name']
    industryVO.designation = request.form['designation']
    industryVO.work_description = request.form['work_description']
    industryVO.no_of_months = request.form['no_of_months']
    
    #courseVO.department = department
    login_Id = loginDAO.fetchId(loginVO)
    industryVO.industry_loginId = login_Id
    
    if request.form['Id'] == 'Null':
        industryDAO.insertIndustryExp(industryVO)
    else:
        industryVO.Id = request.form['Id']
        industryDAO.updateIndustryExp(industryVO)

    session['currentPage'] = 'experience'
    return redirect(url_for("userProfile"))

@app.route('/deleteIndustryExp', methods=["GET"])
def deleteIndustryExp():
    industryVO = IndustryVO()
    industryDAO = IndustryDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    login_Id = loginDAO.fetchId(loginVO)
    industryVO.industry_loginId = login_Id
    Id = request.args.get('Id')
    industryVO.Id = Id
    industryDAO.deleteIndustryExp(industryVO)
    session['currentPage'] = 'experience'
    return redirect(url_for("userProfile"))

@app.route('/insertPersonalInfo', methods=["POST"])
def insertPersonalInfo():    
    personalVO = PersonalVO()
    personalDAO = PersonalDAO()
    signupVO = SignUpVO()
    signupDAO = SignUpDAO()

    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    #Id = request.args.get('Id')
    #course_no = request.form['course_no'+str(Id)]
    #department = request.form['department']
    id = loginDAO.fetchId(loginVO)

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    contact_email = request.form['contact_email']
    contact_number = request.form['contact_number']
    address = request.form['address']
    description = request.form['description']

    signupVO.firstname = firstname
    signupVO.lastname = lastname
    signupVO.signup_LoginId = id
    personalVO.personal_loginId = id
    personalVO.contact_email = contact_email
    personalVO.contact_number = contact_number
    personalVO.address = address
    personalVO.description = description
    
    if request.form['Id'] == 'Null':
        personalDAO.insertPersonal(personalVO)
    else:
        personalVO.Id = request.form['Id']
        personalDAO.updatePersonal(personalVO)
    
    signupDAO.updateUser(signupVO)

    session['currentPage'] = 'personal_information'
    return redirect(url_for("userProfile"))

@app.route('/insertEducation', methods=["GET","POST"])
def insertEducation():
    
    educationVO = EducationVO()
    educationDAO = EducationDAO()


    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    #Id = request.args.get('Id')
    #course_no = request.form['course_no'+str(Id)]
    #department = request.form['department']
    id = loginDAO.fetchId(loginVO)

    degree_name = request.form['degree_name']
    start_date = request.form['start_date']
    institution_name = request.form['institution_name']
    end_date = request.form['end_date']
    cgpa = request.form['cgpa']
    
    educationVO.degree_name = degree_name
    educationVO.start_date = start_date
    educationVO.institution_name = institution_name
    educationVO.end_date = end_date
    educationVO.cgpa = cgpa
    educationVO.education_loginId = id
    
    if request.form['Id'] == 'Null':
        educationDAO.insertEducation(educationVO)
    else:
        educationVO.Id = request.form['Id']
        educationDAO.updateEducation(educationVO)
    
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))

@app.route('/insertProject', methods=["POST"])
def insertProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    

    loginVO.email = session['login_email']
    
    projectVO.project_title = request.form['project_title']
    projectVO.project_detail = request.form['project_detail']
    projectVO.project_loginId = loginDAO.fetchId(loginVO)
    print('=------------------------------')
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
    
    projectDAO.insertProject(projectVO)
    session['currentPage'] = 'skills'

    return redirect(url_for("userProfile"))
@app.route('/deleteProject', methods=["GET"])
def deleteProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    login_Id = loginDAO.fetchId(loginVO)
    projectVO.project_loginId = login_Id
    Id = request.args.get('Id')
    projectVO.Id = Id
    projectDAO.deleteProject(projectVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))
@app.route('/updateProject', methods=["GET","POST"])
def updateProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    projectVO.project_title = request.form['project_title'+str(Id)]
    projectVO.project_detail = request.form['project_detail'+str(Id)]
    projectVO.Id = Id
    #loginId = loginDAO.fetchId(loginVO)
    projectDAO.updateProject(projectVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))
