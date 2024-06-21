__Program__     = "GoogleSheetAPIs.WorkBookFunctions"    
__Programer__   = "Themadhood Pequot"
__Date__        = "6/21/2024"
__Version__     = "0.0.1"
__Update__      = ""
__Info__        = ""

#imports
try:
    from .SheetFunctions import *
except:
    from SheetFunctions import *

VersionLst += [f"{__Program__}: {__Version__}"]


#########################################################################
######################### sheet compiling ###############################
#########################################################################

def LstCompile(workBook:dict):
    lst = []
    for sheet, records in workBook.items():
        for record in records:
            lst.append(record)
    return lst

def DictCompile(workBook:dict,PrimeryKey:str):
    dct = {}
    for sheet, records in workBook.items():
        for record in records:
            dct.update({record[PrimeryKey]:record})
    return dct

def DictListCompile(workBook:dict,PrimeryKey:str):
    dct = {}
    lst = []
    for sheet, records in workBook.items():
        for record in records:
            lst.append(record)
            dct.update({record[PrimeryKey]:record})
    return dct,lst

#########################################################################
################################# other #################################
#########################################################################

def RemoveBlanksFromWorkBookDataSet(DataSet:dict,PrimeryKey:str,Error=False):
    for sheet, records in DataSet.items():
        DataSet[sheet] = RemoveBlanksFromSheetDataSet(records,PrimeryKey,Error)


if __name__ == "__main__":
    Error.VershonRecordsLog(pyName=__Program__,msg=VersionLst)

#index.title#name of sheet
"""
#change sheet
sheet = WorkBook.worksheet("Ornithischia")
#get all Records as list of dcts
dataSet1 = sheet.get_all_records()
#create Sheet
newsheet = gsheet.add_worksheet(title="New Worksheet", rows="100", cols="20")
#delete sheet
gsheet.del_worksheet(newsheet)
#get cell value
cval = wsheet.acell('A2').value
#update cell value
wsheet.update('A2', 'John')
#get all row valls
row_index = 2
values_row = wsheet.row_values(row_index)
#get all colum values
col_index = 3
values_column = wsheet.col_values(col_index)
#insert new row
student_data = ['Emily', 'Watson', 89]
new_row_index = 6
wsheet.insert_row(student_data, new_row_index)
"""




