import os 
from openpyxl import load_workbook
from openpyxl import Workbook

def merge_file(path,output_file):

    print(path)

    fileList=os.listdir(path)

    wkbk = Workbook()

    for file in fileList:
        wb = load_workbook(path+file)
        print(wb.sheetnames[0])
 
        outsheet = wkbk.create_sheet(wb.sheetnames[0]) 
        for sheet in wb:
            print("max row=",sheet.max_row,"max column=",sheet.max_column)
            for i in  range(1,sheet.max_row+1):
                for j in range(1,sheet.max_column+1):
#                    print((outsheet.cell(row=i, column=j)))
                    outsheet.cell(row=i, column=j,value=sheet.cell(row=i, column=j).value)


    wkbk.remove(wkbk.get_sheet_by_name("Sheet"))

    wkbk.save(output_file)


if __name__ == "__main__":

    merge_file("./device-log/","merge.xlsx")


