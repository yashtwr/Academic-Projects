from project import app
import unittest



class FlaskTestCases(unittest.TestCase):
    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Sign Up' in response.data)

    def test_correct_signup(self):
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        
        self.assertTrue(response, "/login")

    def test_incorrect_signup(self):
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        self.assertIn(b'User already exists!', response.data)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Forgot Password?' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        self.assertTrue(b'Welcome admin@uwaterloo00.ca.', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="tester@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Login Failed!', response.data)

    def test_forgotPassword(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_forgotPassword_loads(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertTrue(b'Save' in response.data)

    def test_forgotPassword_change_password(self):
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo00.ca", confirmpswd="Abcd12345"),
                               follow_redirects=True)
        self.assertTrue(response, "/login")

    def test_forgotPassword_no_user_exist(self):
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo009.ca", confirmpswd="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Please enter valid username.',response.data)

    def test_aboutUs(self):
        tester = app.test_client(self)
        response = tester.post('/AboutUs', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_aboutUs_page(self):
        tester = app.test_client(self)
        response = tester.post('/AboutUs', content_type='html/text')
        self.assertTrue(b'About Us' in response.data)

    def test_dashboard(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/loadDashboard', content_type='html/text',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/loadDashboard', content_type='html/text')
        self.assertTrue(b'Search based on Filters' in response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/userLogoutSession',follow_redirects=True)
        self.assertTrue(response, "/login")

    


if __name__ == '__main__':
    unittest.main()
