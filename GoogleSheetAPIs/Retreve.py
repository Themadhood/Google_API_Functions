__Program__     = "GoogleSheetAPIs.Retreve"    
__Programer__   = "Themadhood Pequot"
__Date__        = "5/8/2023"
__Version__     = "0.0.3"
__Update__      = "Documentation"
__Info__        = "Fetches records"

#imports
try:
    from .Open import *
except:
    from Open import *

VersionLst += [f"{__Program__}: {__Version__}"]

_gspread = Error.gspread
_ServiceAccountCredentials = Error.ServiceAccountCredentials
_time = Error.time


def FetchAllFrombook(URL,credentials,error=False,Log=True):
    start = _time.time()
    RC_DCT = dict()

    #open work book
    gc,WorkBook = GetWorkBook(URL,credentials)
    #get all sheets in work book
    sheets = WorkBook.worksheets()
    
    #get all recods from all the sheets
    while sheets > []:
        SheetName = sheets.pop().title
        if Log:
            Error.Log(f"fetching records from {SheetName}","Log.txt")
        sheet = WorkBook.worksheet(SheetName)
        DataSet = _GetAllFromSheet(sheet,error=error)
        RC_DCT.update({SheetName:DataSet})
        _time.sleep(4)

    gc.session.close()
    
    end = _time.time()
    RunTime = int(end - start)
    if Log:
        Error.Log(f"Fetch all records from google sheet {WorkBook.title} run \
time: {RunTime}s","Log.txt")
    return RC_DCT


def GetAllFromSheet(URL,SheetName,credentials,error=False,Log=True):
    start = _time.time()

    #open work book
    gc,WorkBook,Sheet = GetWorkSheet(SheetName,URL,credentials)
    #get all sheets in work book
    data = _GetAllFromSheet(Sheet,error=error)

    gc.session.close()
    
    end = _time.time()
    RunTime = int(end - start)
    if Log:
        Error.Log(f"Fetch all records from google sheet {WorkBook.title}.\
{SheetName} run time: {RunTime}s","Log.txt")
    return data




def _GetAllFromSheet(Sheet,Retry=0,error=False):
    FailCount = 0
    msg = ""
    while True:
        try:
            DataSet = Sheet.get_all_records()
            break
        except IndexError:
            DataSet = []
            break
        except Exception as e:
            if Retry > 5:
                Error.Log(f"{msg} retry failed to many times")
                return dict()
            
            FailCount += 1
            msg = f"Faild to load {Sheet} records \
{FailCount} times {Retry} Retry"
                
            if FailCount > 100:
                Error.UploadError([__Program__,__version__,
                                       "","_GetAllFromSheet",msg,e],
                                  "GoogleSheet")
                _time.sleep(30)
                while True:
                    try:
                        return _GetAllFromSheet(workbook,SheetName,Retry+1,
                                                error)
                    except:
                        Retry+=1
    return DataSet

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




