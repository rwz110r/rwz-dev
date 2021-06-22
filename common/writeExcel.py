import xlrd,os
from xlutils.copy import copy
class WriteExcel():
    def __init__(self):
        self.file_path = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.xlsx'
        # self.sheet = xlrd.open_workbook(self.file_path).sheet_by_index(0)
        with xlrd.open_workbook(self.file_path) as self.rb:
            self.wb =copy(self.rb)
        self.ws = self.wb.get_sheet(0)
    def write(self,id,real,status):
        self.ws.write(id,6,real)
        self.ws.write(id,7,status)
        self.wb.save(self.file_path)
we = WriteExcel()

if __name__ == '__main__':
    we.write(1,0,0)


