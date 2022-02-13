from project import db

from project.com.vo.LoginVO import LoginVO

class LoginDAO:
	def insertLogin(self, loginVO):
		print('inside LoginDAO')
		db.session.add(loginVO)
		db.session.commit()

	def validateLogin(self, loginVO):
		loginList = LoginVO.query.filter_by(userId = loginVO.userId, password = loginVO.password)
		return loginList

	def validateUser(self, loginVO):
		loginList = LoginVO.query.filter_by(userId = loginVO.userId)
		return loginList

	def updatePassword(self, loginVO):
		loginList = LoginVO.query.filter_by(userId = loginVO.userId).first()
		loginList.password = loginVO.password
		db.session.commit()