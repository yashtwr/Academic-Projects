from project import db
from project.com.vo.CoursesVO import CoursesVO


class CoursesDAO:
    # insert into database
    def insertCourses(self, coursesVO):
        db.session.add(coursesVO)
        db.session.commit()

    # fetch records from database
    def fetchCourses(self, coursesVO):
        courses_list = CoursesVO.query.filter_by(course_loginId=coursesVO.course_loginId).all()
        return courses_list

    # delete records from database
    def deleteCourses(self, coursesVO):
        CoursesVO.query.filter_by(course_no=coursesVO.course_no, course_loginId=coursesVO.course_loginId).delete()
        db.session.commit()

    def updateCourses(self, coursesVO):
        db.session.merge(coursesVO)
        db.session.commit()

