__Program__     = "GoogleSheetAPIs.GetVersion"    
__Programer__   = "Themadhood Pequot"
__Date__        = "11/15/2023"
__Version__     = "0.0.2"
__Update__      = "Documentation"
__Info__        = "get spesific virsion"


import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
    from .Retreve import *
except:
    from Retreve import *

VersionLst += [f"{__Program__}: {__Version__}"]

import io,os,time,sys
if getattr(sys, 'frozen', False):
    _FP = os.path.dirname(sys.executable)
elif __file__:
    _FP = os.path.dirname(__file__)


try:
    from THEMADHOOD.URLsCredentals import VersionURL,VersionCredentals
    _URL = VersionURL
    _Credentals = VersionCredentals
except:
    _URL = ""
    _Credentals = ""

def GetVersion(Type,List=None,error=False,url=_URL,Credentals=_Credentals):
    """
List type None returns all max Version URLs in sheet as dct
List type str returns max Version URL as dct
List type list returns max Version URLs in list as dct
List type dct returns max Version URLs in not in keys and version > than key as dct
"""
    retar = {}
    data = GetAllFromSheet(URL,Type,Credentals)
    keys = list(data[0])
    keys.remove("Version")
    for v in data:
        vkeys = keys.copy()
        for key in vkeys:
            if v[key] != "FALSE":#if spesified url None or url
                retar.update({key:{"Version":v["Version"],
                                              "URL":v[key]}})
            else:#if key dosent have update url
                keys.remove(key)

                
    if type(List) == str:
        return retar[List]
    
    elif type(List) == list:
        pop = list(retar)
        #remove items from list of items to pop
        for l in List:
            if l in pop:
                pop.remove(l)
        #remove items not in List
        for p in pop:
            retar.pop(p)
            
    elif type(List) == dict:
        keys = list(List)
        retarkeys = list(retar)
        for k in keys:
            if k in retarkeys:
                if CheckVersionGreater(List[k],retar[k]["Version"],error):
                    pass
                else:
                    retar.pop(k)
                    

    return retar

def CheckVersionGreater(current,check,error=False):
    current = current.split(".")
    check = check.split(".")
    if int(current[0]) < int(check[0]):
        return True
    elif int(current[1]) < int(check[1]):
        return True
    elif int(current[2]) < int(check[2]):
        return True
    return False


if __name__ == "__main__":
    Error.VershonRecordsLog(pyName=__Program__,msg=VersionLst)
    data = GetVersion("Apps",{'EVG URL':"12.0.0","X18 URL":"1.0.0"})
    print(data)







