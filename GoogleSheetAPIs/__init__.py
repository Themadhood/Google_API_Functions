__Program__     = "GoogleSheetAPIs.__init__"    
__Programer__   = "Themadhood Pequot"
__Date__        = "5/8/2023"
__Version__     = "0.0.4"
__Update__      = "Documentation"
__Info__        = ""

#imports
try:
    from .WorkBookFunctions import *
except:
    from WorkBookFunctions import *

VersionLst += [f"{__Program__}: {__Version__}"]



if __name__ == "__main__":
    Error.VersionRecordsLog(pyName=__Program__,msg=VersionLst)

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




