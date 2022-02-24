import email
from project import app
import unittest

class FlaskTestCases(unittest.TestCase):
    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_signup_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Please fill in this form to create an account.' in response.data)

    def test_correct_signup(self):
        tester = app.test_client(self)
        tester.get('/signup',content_type='html/text')
        response = tester.post('/insertUser',data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo.ca", password="Abcd1234", confirmpassword="Abcd1234", gender="female", category="student"), follow_redirects=True)
        self.assertTrue(response.request.path, "/login")

    def test_incorrect_signup(self):
        tester = app.test_client(self)
        tester.get('/signup',content_type='html/text')
        response = tester.post('/insertUser',data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo.ca", password="Abcd1234", confirmpassword="Abcd1234", gender="female", category="student"), follow_redirects=True)
        self.assertIn(b'User already exists!', response.data)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Forgot Password?' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',data=dict(email="admin@uwaterloo.ca", password="Abcd1234"), follow_redirects=True)
        self.assertIn(b'Welcome admin@uwaterloo.ca!', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',data=dict(email="tester@uwaterloo.ca", password="Abcd1234"), follow_redirects=True)
        self.assertIn(b'Login Failed!', response.data)

    def test_forgotPassword(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_forgotPassword_loads(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertTrue(b'Save' in response.data)


if __name__ == '__main__':
    unittest.main()