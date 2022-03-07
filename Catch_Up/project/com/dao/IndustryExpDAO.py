from project import db
from project.com.vo.IndustryExpVO import IndustryVO

class IndustryDAO:
    def insertIndustryExp(self, industryVO):
        db.session.add(industryVO)
        db.session.commit()

    def fetchIndustryExp(self, id):
        Experience_list = IndustryVO.query.all(industry_loginId = id)
        return Experience_list