import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from common.configEmail import ConfigEmail

#用例的所在目录
case_dir = os.path.dirname(os.path.abspath(__file__)) + '\\testCase'

# 2-使用Testloader查找测试用例
def create_suite():
    suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py')
    return suite

#3 自动清理报告
def auto_clear():
    reportfile = os.path.dirname(__file__)+'/report'
    print(os.listdir(reportfile))
    if len(os.listdir(reportfile))>6:
        os.remove(reportfile+'/'+os.listdir(reportfile)[0])

if __name__ == '__main__':
    suite = create_suite()
    timestr = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    filename = os.path.dirname(__file__) + '/report/report' + timestr + '.html'
    with open(filename,'wb') as fb:
        runner = HTMLTestRunner(stream=fb, title='接口自动化测试报告', description='玩安卓项目')
        runner.run(suite)
    ce = ConfigEmail()
    ce.send_email(filename)
    auto_clear()
