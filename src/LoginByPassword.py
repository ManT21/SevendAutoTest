import requests
import unittest

mobile = "13400000004"
r = requests.post('http://10.40.11.177:55851/sevend/login',\
                  data={'en': '1', 'mobile': mobile, 'pwd': 'DkHoLfTQyQ34uqPhaO5F+PcvRKo0/9U4JYYc2RxqcTW2QEpiLTzgaxEm4jdmVMZmdiiMrKo12+zX1t4Vfh9KK/ez3e4AjjuMjGRfU8wtPKOBogYyXb8SZ++dErcFIt1gBWH1RFu+dtV4hmLpgE3RpjHjauUxPIbg+Zd4DZjrPxs=', })
print(r.text)
