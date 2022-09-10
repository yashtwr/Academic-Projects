from project import db

from project.com.vo.SignUpVO import SignUpVO

class SignUpDAO:
    def insertUser(self,signupVO):
        db.session.add(signupVO)
        db.session.commit()
