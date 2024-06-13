__Program__     = "GoogleSheetAPIs.__init__"    
__Programer__   = "Themadhood Pequot"
__Date__        = "5/8/2023"
__Version__     = "0.0.4"
__Update__      = "Documentation"
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

def _insert_key_value(a_dict, key, pos_key, value):
    """new_dict = _OrderedDict()
    for k, v in a_dict.items():
        if k==pos_key:
            new_dict[key] = value  # insert new key
        new_dict[k] = v"""
    dct=dict()
    for k, v in a_dict.items():
        if k==pos_key:
            dct.update({key:value})
        dct.update({k:v})
    return dct

def _ListFormat(keys,dct):
    for key in keys:
        if dct[key] == "":
            dct[key]=[]
        else:
            dct[key]=dct[key].split(",")
    return dct

def RemoveBlanks(DataSet,NKey,Alist=None,Adct=None,
                 Keys_values=None,fkeys=None):
    """DataSet a list of dicts,
NKey a Key to be used as the name,
Alist a list to apend to
Adct a dict to append to
Key_values a dctonary of a Key:[Place new key befor key,Value of new key]
fkeys a list of keys to format to list"""
    lst=[]
    Slst=[]
    if Alist != None:
        lst = Alist
    dct=dict()
    if Adct != None:
        dct = Adct

    while DataSet > []:
        record = DataSet.pop(0)
        if Keys_values != None:
            record = _AddKeysTodct(Keys_values,record)
        if record[NKey] != "":
            #format Record
            if fkeys != None:
                record = _ListFormat(fkeys,record)
            lst.append(record)
            Slst.append(record)
            dct.update({record[NKey]:record})
        else:
            break
    return lst,dct,Slst

def LstCompile(clst,lst):
    copy = lst.copy()
    while copy > []:
        clst.append(copy.pop())

def dctCompile(dct,nkey,lst):
    copy = lst.copy()
    while copy > []:
        record = copy.pop()
        dct.update({record[nkey]:record})

def dctlstCompile(clist,dct,nkey,lst):
    copy = lst.copy()
    while copy > []:
        record = copy.pop()
        clist.append(record)
        dct.update({record[nkey]:record})
            
def MakeBlank(keys,fkeys=None):
    blank = dict()
    for key in keys:
        blank.update({key:""})
    if fkeys != None:
        blank = _ListFormat(fkeys,blank)
    return blank

def _AddKeysTodct(Keys_values,record):
    keys = list(Keys_values)
    for key in keys:
        record = _insert_key_value(record,key,Keys_values[key][0],
                                  _valueKey(Keys_values[key][1]))
    return record

def _valueKey(value):
    if type(value)== list:
        return list()
    return value

def WipeExceptFrozen(sheetname,BotomfrozenRow,URL,credentials):
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

def UplodeRecord(sheetname,insertRow,Record,URL,credentials,
                 color={'red':1,'green':1,'blue':1}):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #insert new row
    sheet.insert_row(Record, insertRow)
    #change color
    sheet.format("2:2",{'backgroundColor':color})
    #Logout
    gc.session.close()

def AppendRecord(sheetname,Record,URL,credentials):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #insert new row
    sheet.append_row(Record)
    #Logout
    gc.session.close()

def SetCell(sheetname,col,row,value,URL,credentials,**kward):
    #Login get sheet
    gc,WorkBook,sheet = GetWorkSheet(sheetname,URL,credentials)
    #update Cell
    sheet.update(f"{col}{row}",value,**kward)
    #Logout
    gc.session.close()

def FindCell(sheetname,value,URL,credentials):
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

def UpdateRecord(sheetname,col1,col2,row,value,URL,credentials):
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




