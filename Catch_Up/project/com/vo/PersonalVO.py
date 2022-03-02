from project import db
from project.com.vo.LoginVO import LoginVO

class PersonalVO(db.Model):
    __tablename__ = "personalmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    description = db.Colum('description', db.String(200), nulllable=False)
    contact_number = db.Column('contact_number', db.Integer)
    contact_email = db.Column('contact_email', db.String(50))
    address = db.Column('address', db.String(200))
    linkedIn_account = db.Column('linkedIn_account', db.String(100))
    other_links = db.Column('other_links', db.String(100))
    personal_loginId = db.Column('personal_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'description': self.description,
            'contact_number': self.contact_number,
            'contact_email': self.contact_email,
            'address': self.address,
            'linkedIn_account': self.linkedIn_account,
            'other_links': self.other_links
        }

db.create_all()