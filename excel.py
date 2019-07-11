from openpyxl import load_workbook
from openpyxl import Workbook

#wkbk = load_workbook('merge.xlsx')

wkbk = Workbook()

#excelfiles = [r'10000021_MessagesExport_2019-07-09.xlsx', r'10000077_MessagesExport_2019-07-04.xlsx']

excelfiles = [r'10000021_MessagesExport_2019-07-09.xlsx']


for file in excelfiles:
    wb = load_workbook(file)
    print(wb.sheetnames[0])
 
    outsheet = wkbk.create_sheet(wb.sheetnames[0]) 
    for sheet in wb:
        print("max row=",sheet.max_row,"max column=",sheet.max_column)
        for i in  range(1,sheet.max_row+1):
            for j in range(1,sheet.max_column+1):
#                print((outsheet.cell(row=i, column=j)))
                outsheet.cell(row=i, column=j,value=sheet.cell(row=i, column=j).value)


wkbk.remove(wkbk.get_sheet_by_name("Sheet"))

wkbk.save("merge.xlsx")






