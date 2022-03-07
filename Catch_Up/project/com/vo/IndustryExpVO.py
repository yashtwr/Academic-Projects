from project import db
from project.com.vo.LoginVO import LoginVO

class IndustryVO(db.Model):
    __tablename__ = "industrymaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column('company_name',db.String(50))
    designation = db.Column('designation',db.String(50))
    work_description = db.Column('work_description',db.String(200))
    start_year = db.Column('start_year', db.Integer)
    end_year = db.Column('end_year', db.Integer)
    industry_loginId = db.Column('industry_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'company_name': self.company_name,
            'designation': self.designation,
            'work_description': self.work_description,
            'start_year': self.start_year,
            'end_date': self.end_year
        }

db.create_all()