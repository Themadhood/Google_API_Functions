__Program__     = "GoogleSheetAPIs.RecordFunctions"    
__Programer__   = "Themadhood Pequot"
__Date__        = "6/21/2024"
__Version__     = "0.0.1"
__Update__      = ""
__Info__        = ""

#imports
try:
    from .SheetUpdate import *
except:
    from SheetUpdate import *

VersionLst += [f"{__Program__}: {__Version__}"]


def AddKeyToRecord(record:dict, key_value:dict):
    for k, v in key_value.items():
        record.update({k:v})
    return record

def Record_Insert_key(record:dict, key, KeyAfter, value):
    dct=dict()
    for k, v in record.items():
        
        if k==KeyAfter:
            dct.update({key:value})
            
        dct.update({k:v})
        
        if KeyAfter == "":
            dct.update({key:value})
    return dct


#########################################################################
######################### Formating #####################################
#########################################################################

def ListFormat(record,keys,SplitKey=","):
    for key in keys:
        if record[key] == "":
            record[key] = []
        else:
            record[key] = record[key].split(SplitKey)
    return record

def DictFormat(record,keys,ValueSplitKey=":",SplitKey=","):
    for key in keys:
        if record[key] == "":
            record[key] = {}
        else:
            dct = record[key].split(SplitKey)
            record[key] = {}
            for element in dct:
                e = element.split(ValueSplitKey)
                record[key].update({e[0]:e[1]})
    return record

#########################################################################
############################# Other #####################################
#########################################################################

def MakeBlank(FiledRecord):
    blank = dict()
    for k, v in FiledRecord.items():
        if type(v) == list:
            blank.update({key:[]})
        elif type(v) == dict:
            blank.update({key:{}})
        elif type(v) == int:
            blank.update({key:0})
        elif type(v) == set:
            blank.update({key:set()})
        else:
            blank.update({key:""})
    return blank
    

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




