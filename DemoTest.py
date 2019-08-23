import requests
import unittest
import HTMLTestRunner
import commonfunction
import time
import rsamethod


class LoginTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_login_by_right_password(self):
        mobile = '13400000039'
        password = '123456'
        result = commonfunction.login_by_password(mobile, password)
        session_key = commonfunction.get_session_key_by_mobile(mobile)
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['data']['session_key'], session_key)

    def test_login_by_wrong_password(self):
        mobile = '13400000039'
        password = '123457'
        result = commonfunction.login_by_password(mobile, password)
        self.assertEqual(result['code'], '3011')
        self.assertEqual(result['data'], None)
        self.assertEqual(result['msg'], '请输入正确的登录密码')


    def tearDown(self):
        pass


if __name__ == '__main__':
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_login_by_wrong_password"))
    filename = './result/'+now+'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告2019',
                                           description='登录功能')
    runner.run(suite)
    fp.close()
