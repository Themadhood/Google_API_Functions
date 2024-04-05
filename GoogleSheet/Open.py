#program:       Open
#purpose:       Fetches records
#progamer:      Madison Arndt 5/8/2023

_FILE = "GoogleSheet.Open"
_VERSION = "0.0.1"

#imports
from THEMADHOOD.Library import Error
    
_gspread = Error.gspread
_ServiceAccountCredentials = Error.ServiceAccountCredentials
_time = Error.time

def Login(credentials):
    #Login
    try:
        gc = _gspread.service_account(filename=credentials)
    except:
        gc = _gspread.service_account_from_dict(credentials)
    return gc

def GetWorkBook(URL,credentials):
    #Login
    gc = Login(credentials)
    #open work book
    WorkBook = gc.open_by_url(URL)

    return gc,WorkBook

def GetWorkSheet(sheetname,URL,credentials):
    #Login and open work book
    gc,WorkBook = GetWorkBook(URL,credentials)
    
    #change sheet
    sheet = WorkBook.worksheet(sheetname)

    return gc,WorkBook,sheet




if __name__ == "__main__":
    creds = 'Personal.json'
    URL = "https://docs.google.com/spreadsheets/d/1w-m8cuFOS9XALMbeo7kJplmPTBlgxK2pSa95H-pEBm8/edit?usp=sharing"

    gc,wb,sheet = GetWorkSheet("Food",URL,creds)

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




