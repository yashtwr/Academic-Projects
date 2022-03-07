from project import db
from project.com.vo.LoginVO import LoginVO

class CertificatesVO(db.Model):
    __tablename__ = "certificatesmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    certificates = db.Column('certificates',db.String(20))
    certificates_loginId = db.Column('certificates_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'certificates': self.certificates
        }

db.create_all()