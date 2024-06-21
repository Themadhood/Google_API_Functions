__Program__     = "GoogleSheetAPIs.SheetUpdate"    
__Programer__   = "Themadhood Pequot"
__Date__        = "6/21/2024"
__Version__     = "0.0.1"
__Update__      = ""
__Info__        = ""

#imports
try:
    from .Colors import *
    from .GetVersion import *
except:
    from Colors import *
    from GetVersion import *

VersionLst += [f"{__Program__}: {__Version__}"]
    
_gspread = Error.gspread
_ServiceAccountCredentials = Error.ServiceAccountCredentials
_time = Error.time


def WipeExceptFrozen(URL,credentials,sheetname,BotomfrozenRow=0):
    start = _time.time()
    RC_DCT = dict()
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #insert blank row
    row = BotomfrozenRow +1
    sheet.insert_row([], row)
    sheet.format(f"{row}:{row}",{ 'backgroundColor': {'red':1,
                                                      'green':1,
                                                      'blue':1}})
    #delete rows
    sheet.resize(rows=row)

    gc.session.close()
    
    end = _time.time()
    RunTime = int(end - start)
    Error.Log(f"wipe worksheet {sheetname} run time: \
{RunTime}s","Log.txt")

def UplodeRecord(URL,credentials,sheetname,insertRow,Record,
                 color={'red':1,'green':1,'blue':1}):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #insert new row
    sheet.insert_row(Record, insertRow)
    #change color
    sheet.format("2:2",{'backgroundColor':color})
    #Logout
    gc.session.close()

def AppendRecord(URL,credentials,sheetname,Record):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #insert new row
    sheet.append_row(Record)
    #Logout
    gc.session.close()

def SetCell(URL,credentials,sheetname,col,row,value,**kward):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #update Cell
    sheet.update(f"{col}{row}",value,**kward)
    #Logout
    gc.session.close()

def FindCell(URL,credentials,sheetname,value):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #update Cell
    cell = sheet.find(value)
    try:
        retar = (cell.row,cell.col)
    except:
        retar = None
    #Logout
    gc.session.close()

    return retar

def UpdateRecord(URL,credentials,sheetname,col1,col2,row,value):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #update Cell
    sheet.update(f"{col1}{row}:{col2}{row}",[value])
    #Logout
    gc.session.close()


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




