from project import db
from project.com.vo.CertificatesVO import CertificatesVO

class CertificatesDAO:
    def insertSkills(self, certificatesVO):
        db.session.add(certificatesVO)
        db.session.commit()

    def fetchcertificates(self, id):
        certificates_list = CertificatesVO.query.all(certificates_loginId = id)
        return certificates_list