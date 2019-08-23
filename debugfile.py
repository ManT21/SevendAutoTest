import requests
import redisdb
import mysql


def test_login_by_password():
    base_url = "http://10.40.11.177:55851/sevend/login"
    account = {'mobile': '13400000069', 'verify_key': 'af41e2fb-12bb-47ce-abab-855c886918c8',
                    'pwd': 'YWzpiegCW/tEW0FbtDQWyTHWSLZM0mGn2GOUAbJU3w349UxKXQ46O'
                           '+7AT28OOnViegouRil5eBsakRiyCSAdWNl5yZhno1+1Tema'
                           '//YN0KctjHbgQEHCidsV8MvscvfycSY7jlwIkd0D4tit9WKf+MQhJFMU'
                           '/hLAh9p3O5zJxmY='}
    sql = "SELECT id FROM sevend.t_customer WHERE mobile = %s" % (account['mobile'])
    res = mysql.fetchonedb(sql)
    customerId = str(res['id'])
    #customerId = '2903255'
    r = requests.post(base_url, data=account)
    result = r.json()
    value = redisdb.get_key('session_' + customerId)
    #self.assertEqual(result['code'], '0')
    print(result)
    print(result['data']['session_key'])
    print(bytes.decode(value))
    if result['data']['session_key'] == bytes.decode(value):
        print('yes')
    else:
        print('no')


test_login_by_password()
