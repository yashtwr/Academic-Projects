from project import db
from project.com.vo.IndustryExpVO import IndustryVO

class IndustryDAO:
    def insertIndustryExp(self, industryVO):
        db.session.add(industryVO)
        db.session.commit()

    def fetchIndustryExp(self, industryVO):
        Experience_list = IndustryVO.query.filter_by(industry_loginId = industryVO.industry_loginId).all()
        return Experience_list
