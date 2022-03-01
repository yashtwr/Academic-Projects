from project import db
from project.com.vo.CoursesVO import CoursesVO

class CoursesDAO:
    def insertCourses(self, coursesVO):
        db.session.add(coursesVO)
        db.session.commit()

    def fetchEdu(self, id):
        courses_list = CoursesVO.query.all(education_loginId = id)
        return courses_list