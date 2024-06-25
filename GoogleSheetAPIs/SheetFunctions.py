__Program__     = "GoogleSheetAPIs.SheetFunctions"    
__Programer__   = "Themadhood Pequot"
__Date__        = "6/21/2024"
__Version__     = "0.0.1"
__Update__      = ""
__Info__        = ""

#imports
try:
    from .RecordFunctions import *
except:
    from RecordFunctions import *

VersionLst += [f"{__Program__}: {__Version__}"]

def RemoveBlanksFromSheetDataSet(DataSet:list,PrimeryKey:str,Error=False):
    DataSet = DataSet.copy()
    retar = []
    while DataSet > []:
        record = DataSet.pop(0)
        if record[PrimeryKey] != "":
            retar.append(record)
        else:
            break
    return retar

def SheetListFormat(DataSet:list,keys,SplitKey=","):
    for record in DataSet:
        ListFormat(record,keys,SplitKey)

def SheetDictFormat(DataSet:list,keys,ValueSplitKey=":",SplitKey=","):
    for record in DataSet:
        DictFormat(record,keys,ValueSplitKey,SplitKey)

        

def SheetAddKeyToRecord(DataSet:list, key_value:dict):
    for record in DataSet:
        AddKeyToRecord(record=record, key_value=key_value)

def SheetRecord_Insert_key(DataSet:list, keyAfter_value:dict):
    """keyAfter_value = {"key insert comes after":{key:value}}"""
    for record in DataSet:
        Record_Insert_key(record=record,keyAfter_value=keyAfter_value)
    


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




