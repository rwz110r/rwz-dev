'''
实现步骤：
1.读取excel中的表头作为字典的key
2.遍历次数为1-最大行
3.将遍历的每行的每一个值与第一行的key组成字典并return
'''
import xlrd,os
class ReadExcel():
    def __init__(self):
        self.file_path = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.xlsx'
        self.sheet = xlrd.open_workbook(self.file_path).sheet_by_index(0)
    def getData(self):
        #定义用于存储数据的list
        list1 = []
        for i in range(1,self.sheet.nrows):
            #重置存储每一组数据的字典
            dic1 = {}
            for j in range(len(self.sheet.row_values(i))):
                dic1[self.sheet.row_values(0)[j]] = self.sheet.row_values(i)[j]
            list1.append(dic1)
        return list1
RE = ReadExcel()
testdata = RE.getData()
if __name__ == '__main__':
    wx = ReadExcel()
    print(wx.getData())