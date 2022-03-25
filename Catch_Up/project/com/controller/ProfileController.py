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

        loginVO = LoginVO()
        loginDAO = LoginDAO()
        
        loginVO.email = session['login_email']
        id = loginDAO.fetchId(loginVO)

        courseVO.course_loginId = id
        lst = courseDAO.fetchCourses(courseVO)
        courses = [i.as_dict() for i in lst]
        print('=------------------------------')
        
        certificatesVO.certificates_loginId = id
        lst_certi = certificatesDAO.fetchCertificates(CertificatesVO)
        certificates = [i.as_dict() for i in lst_certi]
        print('---------------------------------')

        industryVO.industry_loginId = id
        lst_industry = industryDAO.fetchIndustryExp(industryVO)
        industryExp = [i.as_dict() for i in lst_industry]
        print('IndustryExperience===========================================')
        print(industryExp)

        if 'currentPage' not in session:
            session['currentPage'] = 'personal_information'

        return render_template("profilesetup_changes.html", title = "profileSetup", courses = courses, certificates = certificates, industryExp = industryExp)
    except Exception as ex:
        print(ex)


@app.route('/insertCourse', methods=["GET","POST"])
def insertCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    courseVO.course_no = request.form['course_no1']
    courseVO.department = request.form['department']
    # courseVO.department = request.args.get('department')
    # courseVO.department = department
    courseVO.course_loginId = loginDAO.fetchId(loginVO)
    print('=------------------------------')
    print(request.args.get('courseid'))
    print(request.args.get('department'))
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')

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
    print('*********************8', Id, course_no, department)
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
    print('=------------------------------')
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
    
    print(request.args.get('certificates'))
    certificatesDAO.insertCertificates(certificatesVO)
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
        print('old one-------------------------------------')
        industryDAO.insertIndustryExp(industryVO)
    else:
        print('Data is updated-------------------------------------')
        print(request.form['Id'])
        print('-------------------------------------')
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




@app.route('/profileSetup', methods=["GET", "POST"])
def profile():
    #course
    course_no = request.form['course_no']
    department = request.form['department']
    #educational details
    degree_name = request.form['degree_name']
    institution_name = request.form['institution_name']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    cgpa = request.form['cgpa']
    #certificates
    certificates = request.form['certificates']
    #hobbies
    hobbies = request.form['hobbies']
    #industry experience
    company_name = request.form['company_name']
    designation = request.form['designation']
    work_description = request.form['work_description']
    no_of_months = request.form['no_of_months']
    #personal details
    description = request.form['description']
    contact_number = request.form['contact_number']
    contact_email = request.form['contact_email']
    address = request.form['address']
    linkedIn_account = request.form['linkedIn_account']
    other_links = request.form['other_links']
    #Project Details
    project_title = request.form['project_title']
    project_detail = request.form['project_detail']
    #skills
    skills = request.form['skills']


    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    educationVO = EducationVO()
    educationDAO = EducationDAO()
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    hobbiesVO = HobbiesVO()
    hobbiesDAO = HobbiesDAO()
    industryVO = IndustryVO()
    industryDAO = IndustryDAO()
    personalVO = PersonalVO()
    personalDAO = PersonalDAO()
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    skillsVO = SkillsVO()
    skillsDAO = SkillsDAO()

    courseVO.course_no = course_no
    courseVO.department = department

    educationVO.degree_name = degree_name
    educationVO.institution_name = institution_name
    educationVO.start_date = start_date
    educationVO.end_date = end_date
    educationVO.cgpa = cgpa

    certificatesVO.certificates = certificates

    hobbiesVO.hobbies = hobbies

    industryVO.company_name = company_name
    industryVO.designation = designation
    industryVO.work_description = work_description
    industryVO.no_of_months = no_of_months

    personalVO.description = description
    personalVO.contact_number = contact_number
    personalVO.contact_email = contact_email
    personalVO.address = address
    personalVO.linkedIn_account = linkedIn_account
    personalVO.other_links = other_links

    projectVO.project_title = project_title
    projectVO.project_detail = project_detail

    skillsVO.skills = skills

    loginVO.email = session['login_email']
    lst = loginDAO.validateUser(loginVO)

    lst = [i.as_dict for i in lst]
    if len(lst) > 0:
        courseVO.course_loginId = loginDAO.fetchId(loginVO)
        courseDAO.insertCourses(courseVO)

        educationVO.education_loginId = loginDAO.fetchId(loginVO)
        educationDAO.insertEducation(educationVO)

        certificatesVO.certificates_loginId = loginDAO.fetchId(loginVO)
        certificatesDAO.insertCertificates(certificatesVO)

        hobbiesVO.hobbies_loginId = loginDAO.fetchId(loginVO)
        hobbiesDAO.insertHobbies(hobbiesVO)

        industryVO.industry_loginId = loginDAO.fetchId(loginVO)
        industryDAO.insertIndustryExp(industryVO)

        personalVO.personal_loginId = loginDAO.fetchId(loginVO)
        personalDAO.insertPersonal(personalVO)

        projectVO.project_loginId = loginDAO.fetchId(loginVO)
        projectDAO.insertProject(projectVO)

        skillsVO.skills = loginDAO.fetchId(loginVO)
        skillsDAO.insertSkills(skillsVO)
        return render_template("show_profile.html", msg1 = "Profile editted successfully", title = "Profile", courses = courseVO, education = educationVO, certificates = certificatesVO, hobbies = hobbiesVO, industry = industryVO, personal = personalVO, project = projectVO, skills = skillsVO)
    else:
        return render_template("signup.html", msg="User already exists!", title = "SignUp")
