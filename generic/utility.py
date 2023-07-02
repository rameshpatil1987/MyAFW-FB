import openpyxl

class Excel:
    def get_cellvalue(path,sheet,row,col):
        wb=openpyxl.load_workbook(path)
        value=wb[sheet].cell(row,col).value
        print("Xl cell value is: ",value)
        return value