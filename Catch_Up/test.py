from project import app, db
import unittest
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SignUpVO import SignUpVO

import pytest

# --------------- WARNING -----------------------------
# This test file will delete the records of data and will use some dummy data to run the tests.


# ------------------ NOTE ------------------------------
# test cases are running in alphabetical orders.
# so to maintain order, tests are assigned names as test_a, test_b etc...


class TestCases(unittest.TestCase):

    # test_signup
    def test_a(self):
        print('***** test_signup *********')
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test_signup_loads
    def test_b(self):
        print('***** test_signup_loads *********')
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Please fill in this form to create an account.' in response.data)

    # test_correct_signup
    def test_c(self):
        print('***** test_correct_signup *********')
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        print(response.data)
        self.assertIn(b'Account created successfully', response.data)


    # test_incorrect_signup
    def test_d(self):
        print('***** test_incorrect_signup *********')
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        self.assertIn(b'User already exists!', response.data)

    # test_login
    def test_e(self):
        print('***** test_login *********')
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test_login_loads
    def test_f(self):
        print('***** test_login_loads *********')
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Forgot Password?' in response.data)

    # test_correct_login
    def test_g(self):
        print('***** test_correct_login *********')
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        print('----------------- :::: ', response.data)
        self.assertIn(b'Welcome', response.data)

    # test_incorrect_login
    def test_h(self):
        print('***** test_incorrect_login *********')
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="tester@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Login Failed!', response.data)

    # test_forgot_password
    def test_i(self):
        print('***** test_forgot_password *********')
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test_forgotpassword_loads
    def test_j(self):
        print('***** test_forgotpassword_loads *********')
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertTrue(b'Save' in response.data)

    # test_forgotpassword_change_password
    def test_k(self):
        print('***** test_forgotpassword_change_password *********')
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo00.ca", confirmpswd="Abcd12345"),
                               follow_redirects=True)

        self.assertIn(b'Password updated successfully.', response.data)

        # test_forgotpassword_no_user_exists

    def test_l(self):
        print('***** test_forgotpassword_no_user_exists *********')
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo009.ca", confirmpswd="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Please enter valid username.', response.data)


if __name__ == '__main__':
    b = db.session.query(SignUpVO).delete()
    a = db.session.query(LoginVO).delete()
    db.session.commit()

    unittest.main()
