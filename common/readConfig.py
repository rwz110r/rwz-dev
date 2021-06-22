import  configparser,os

class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.configfile = os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        self.conf.read(self.configfile,encoding='utf-8')
    def get_section(self,name):
        result = self.conf.items(name)
        return result
    def get_option(self,name,item):
        result = self.conf.get(name,item)
        return result
if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.configfile)
    print(rc.get_section('mysql'))
    print(rc.get_option('mysql','host'))