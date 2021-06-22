import unittest,requests
from common.readExcel import testdata
from common.writeExcel import we
from ddt import ddt,data,unpack
print(testdata)
@ddt
class TestCase(unittest.TestCase):
    @data(*testdata)
    @unpack
    def test_run(self,id,interfaceUrl,name,Method,value,expect,real,status):
        if Method == 'get':
            res = requests.get(interfaceUrl,eval(value))
            real_errorcode = res.json()['errorCode']
            try:
                self.assertEqual(str(res.status_code),'200')
                self.assertEqual(str(real_errorcode),str(expect))
                status = 'success'
            except AssertionError as msg:
                print("系统错误，原因：%s" % msg)
                status = 'fail'
                raise
            finally:
                we.write(id,real_errorcode,status)
        elif Method == 'post':
            res = requests.post(url=interfaceUrl,data=eval(value))
            real_errorcode = res.json()['errorCode']
            try:
                self.assertEqual(str(res.status_code), '200')
                self.assertEqual(str(real_errorcode), str(expect))
                status = 'success'
            except:
                print("预期与实际不一致，原因：%s" % res.json()['errorMsg'])
                status = 'fail'
                raise
            finally:
                we.write(id,real_errorcode,status)

if __name__ == '__main__':
    unittest.main()
    # res1 = requests.post(url='https://www.wanandroid.com/user/register',data={'username':'liangchao03','password':'123456','repassword':'123456'})
    # print(res1.json())