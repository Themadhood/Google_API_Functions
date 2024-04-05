#program:       GetVersion
#purpose:       get spesific virsion
#progamer:      Madison Arndt 11/15/2023

_FILE = "GoogleSheet.GetVersion"
_VERSION = "0.0.1"


import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
    from .Retreve import *
except:
    from Retreve import *

import io,os,time,sys
if getattr(sys, 'frozen', False):
    _FP = os.path.dirname(sys.executable)
elif __file__:
    _FP = os.path.dirname(__file__)

#url ov version work book
_URL = "https://docs.google.com/spreadsheets/d/1b75WVekAmdnDBYseKNmPeni8aO7IHwgI7WnkvvVGjJ8/edit?usp=sharing"
_Credentals = {
  "type": "service_account",
  "project_id": "autoupdate-406200",
  "private_key_id": "7b915d63557fdaa6316848da0573c15c47d7c3c7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDYP7S8Z4jIzmuD\ncgYitGOPQLs/wsbG2awIep1OqFfRraQ4F07BdxhegfE6PzlGYxfQCLjAOqXYQDJm\nAdW+edezpwQMf8ldfbILz4Hvkl6HzIvl9bQWrby5qO68XYHJAt/e1o9RhOgGZyz4\n5LvqFCl4M2QuiI7VCvwLEwgJVGPX2cDuzFBVfdfJ+2exsduUSSlVzGhWWllsKBcI\nGsXO3a4k7+mP1+3udTmQnny902ja7chELsZ9fj+P4//g1uyCXWbE1Zxq5YjlIT/J\niIYTrVymynm/5PfwRaoL8opA4tdXJPGBP3tXMfrMXOCoDCO80RtqKbXxu1ONHlko\neOcU1kqVAgMBAAECggEAASTkkh5Tu3ChSZwzVECtK2jh6Iu20OYuvDtSCI2fgYN3\n11Cbff3U6WOqRvIFHcUl07NNEKX3Kv7Z3ESi1hU5eFYrPAFoyeyT6zgHxHXvDOmA\nQQf/7WulkFQXyn/1Y2x3NS7shYbFzCjHoljP14R3jYLAqt3iJCWCU6G4dG0iU+hU\nds5JdLFKjOy8X9QYNSeSc64DqfRjSie2lK2DOZyyzspgxeMyGl+aToXhVNSucr8V\nGr9suxyufBHa7xwKs+1IrxKwG9TjeMKkds90+bHWN0NFsrp9mqHJNFC4Wobhxv3t\nl4uTv9kB2QKyHN4EY1tISpv9n/w7j17iRYlyty40UQKBgQD2jIEh1rWgRhyjSSrh\nFXTI1hJ0woBP2YX4FQrPafFUFO9k9mmALtkLK5FeNDh39e3RyQ0Tncdersvw/fUx\npRJLT7Igq1UjWlUEhznuy++uQgOeQcfMwrNiXmQqytMoeKmgOJdDim7tv9TAdwbp\n7psjRGsaK7kA4tyMcA8SyzExyQKBgQDgidqf8kSnTCUbkbhCpfJkrCxGv4gvmWGk\nu/jHCGRnYLWw3C7+bHN58YapQRVP2xAR0X4FTxIBfuldt9Bgp9QWXCF34lZAJcsr\nVRGyrdqulXYTlgW4GsXjnXB8valcYITEBdIaBi2cKZMyf0pwN5xGK/hXDt9ywgwh\nzreEVQ9YbQKBgErPi4dnDSma3Km3U+mEhzFBs8v2ENUp3frO977EGNQ4ngN2ucCJ\ndpZrG+sH0XKlDwqvBObE43AZfgycIsBzpD9x6Uz8cBMQH+gF2FBbVVj88vgcYbIC\nCkh498/8R2Jqap4RTeTSpqJBqR7VfyWQn0ZuRklkpvhb3ixG/Gvpd/3xAoGAZdI9\noOCE/3SJM0pOS3LjS4HEBkUepa8hV0miU+dbWIHDgrMmYFuftgGvthr8Zh0J2Xqt\ncgzcNm9ttgD/7oTMqWMYDjxGLoq06i6GewdZrme6hsE2ULlbWY9wjjCXl3txWU7m\nasS4dCNqS7DreZ3OMQgJcrkc3PZf+Ai8sba84bUCgYEApreyZgCry6NZQmGE3vHb\ny8KVLsExFRFnDxZEZ+mXW65pQtrrFg8VCVae9bvteeUiCMl2nMDKTDsTv1ndfV+H\nXxIB+UNJlnsMuUzMUktWgrLbwiGQN5zyngq29eh+8onXOKpaGC+i0/dw1L7wd5du\nSTVUdc69YxI/rLwcoyqWwZA=\n-----END PRIVATE KEY-----\n",
  "client_email": "autoupdate@autoupdate-406200.iam.gserviceaccount.com",
  "client_id": "100027514671797906964",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/autoupdate%40autoupdate-406200.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

def GetVersion(Type,List=None,error=False):
    """
List type None returns all max Version URLs in sheet as dct
List type str returns max Version URL as dct
List type list returns max Version URLs in list as dct
List type dct returns max Version URLs in not in keys and version > than key as dct
"""
    retar = {}
    data = GetAllFromSheet(_URL,Type,_Credentals)
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
    data = GetVersion("Apps",{'EVG URL':"12.0.0","X18 URL":"1.0.0"})
    print(data)







