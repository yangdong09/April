import xlwings as xw
from April_fourth.log.log import logger

class Excel:
    def __init__(self,file_path):
        '''
        初始化函数，需要传入文件路径
        :param file_path: 'E:\test.xls'
        '''
        self.__file_path = file_path

    def open_excle(self,sheetname='Sheet1'):
        '''
        self.__app:不希望修改，所以设为私有变量
        visible：操作excel是否可见。（True可见，False不可见）
        add_book：打开几个excel窗口（True多个。False一个）
        self.book:打开excel工作簿
        :return:
        '''
        self.__app = xw.App(visible=True,add_book=False)
        self.book = self.__app.books.open(self.__file_path)
        self.sht = self.book.sheets[sheetname]

    def get_cell_value(self,col):
        '''
        获取指定单元格或指定范围内容
        :param col: 行号：'a1'或'a1:c5'
        :return:不加.value不能展示单元格中内容
        '''
        try:
            return self.sht.range(col).value
        except Exception as e:
            logger.error('请检查传入参数是否正确，或excel是否已经打开')
            logger.error(e)


    def get_rc_value(self,row,col):
        '''
        通过行，列获取指定单元格的内容
        :param row: 行号：1
        :param col: 列号：2
        :return:
        '''
        try:
            return self.sht[row,col].value
        except Exception as e:
            logger.error(e)

    def get_row_num(self):
        '''
        获取excel总行数
        :return:
        '''
        try:
            return self.sht.used_range.last_cell.row
        except Exception as e:
            logger.error(e)

    def get_col_num(self):
        '''
        获取excel总列数
        :return:
        '''
        try:
            return self.sht.used_range.last_cell.column
        except Exception as e:
            logger.error(e)

#----------------------------一以上获取数据----------------------------------------------------

    def set_row_value(self,row,value):
        '''
        按行写入数据，多个数据写到列表中会从给定的起始位置依次写入
        写入数据excle必须是关闭状态，不关闭会报错（不知道为啥）
        :param row:行：'f2'
        :param value:内容：'写入一个'或'['写','入','多','个']'
        :return:
        '''
        try:
            s = self.sht.range(row).value = value
            return s
        except Exception as e:
            logger.error(e)

    def set_col_value(self,col,value):
        '''
        按列写入数据，多个也是写到列表中
        :param col: 列：'f2'
        :param value: 内容：'写入一个'或'['写','入','多','个']'
        :return:
        '''
        try:
            s = self.sht.range(col).options(transpose=True).value = value
            return s
        except Exception as e:
            logger.error(e)

    def set_table_value(self,table,value):
        '''
        按范围插入数据
        :param table: 起始位置：'f2'
        :param value: 插入内容：[[1,2,3],[4,5,6],[7,8,9]],表示a1:c3范围插入数据
        :return:
        '''
        try:
            s = self.sht.range(table).expand('table').value = value
            return s
        except Exception as e:
            logger.log(e)

    # ----------------------------一以上写入数据----------------------------------------------------

    def save(self,file):
        '''
        保存excel到目录
        :param file: 保存目录：r'D:\qingqiu.xlsx'
        :return:
        '''
        self.book.save(file)

    def close(self):
        '''
        退出book,并关闭excel
        :return:
        '''
        if self.book:
            self.book.close()
        if self.__app:
            self.__app.quit()

if __name__ == '__main__':
    e = Excel(r'D:\Track.xlsx')
    e.open_excle()
    c = e.get_cell_value('a2:c4')
    d = e.set_table_value('f2',[[1,2,3],[4,5,6],[7,8,9]])
    e.save(r'D:\r.xlsx')
    # print(c)
    print(d)
    e.close()
