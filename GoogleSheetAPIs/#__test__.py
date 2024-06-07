

#imports
import gspread
creds = 'Personal.json'
URL = ""

gc = gspread.service_account(filename=creds)
#open work book
WorkBook = gc.open_by_url(URL)
#get sheet in work book
ws = WorkBook.worksheet("Food")

cell = ws.find("BBQ sause")
print(cell)
print("Found something at R%sC%s" % (cell.row, cell.col))

ws.update('A3:D3', [[1, 2, 3, 4]])

#ws.insert_row(["9","8"],2)
    
"""ws.format("2:2", { 'backgroundColor': {
'red':255,
'green':255,
'blue':255}})#"""

#gc.session.close()



"""
#get all sheets in work book
sheets = WorkBook.worksheets()

#change sheet
sheet = WorkBook.worksheet("Name")

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




