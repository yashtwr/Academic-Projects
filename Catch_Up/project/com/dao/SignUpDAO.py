from project import db

from project.com.vo.SignUpVO import SignUpVO

class SignUpDAO:
    def insertUser(self,signupVO):
        db.session.add(signupVO)
        db.session.commit()

    def fetchUser(self, signupVO):
    	signup_list = SignUpVO.query.filter_by(signup_LoginId = signupVO.signup_LoginId).all()
    	return signup_list


    def updateUser(self, signupVO):
    	signup_list = SignUpVO.query.filter_by(signup_LoginId = signupVO.signup_LoginId).first()
    	signup_list.firstname = signupVO.firstname
    	signup_list.lastname = signupVO.lastname
    	db.session.commit()
