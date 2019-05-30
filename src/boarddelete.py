import requests
import json
import hashlib
import threading
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

def getUserid(user_id,user_pw):
    _url = "https://dcid.dcinside.com/join/mobile_app_login.php"
    _hd  = {
    "User-agent" : "dcinside.app",
    "Referer" : "http://www.dcinside.com"
    }
    _data = {
        "user_id" : user_id,
        "user_pw" : user_pw
    }
    req = requests.post(url=_url,headers=_hd,data=_data)
    data = req.json()
    return data[0]["user_id"]



def hashValueToken():
    now = datetime.now()
    str1 = "dcArdchk_%04d%02d%02d%02d" % (now.year,now.month,now.day,now.hour)
    data = hashlib.sha256(str1.encode()).hexdigest()
    return data

def getAppid():
    value_token = hashValueToken()
    _url = "https://dcid.dcinside.com/join/mobile_app_key_verification_3rd.php"
    _hd  = {
    "User-agent" : "dcinside.app",
    "Referer" : "http://www.dcinside.com"
    }
    _data = {
    "value_token" : value_token,
    "signature" : "ReOo4u96nnv8Njd7707KpYiIVYQ3FlcKHDJE046Pg6s=",
    "pkg" : "com.dcinside.app",
    "vCode" : "30037",
    "vName" : "3.2.10"
    }

    req = requests.post(url=_url,headers=_hd,data=_data)
    data = req.json()
    return data[0]["app_id"]



def deletereq(id,app_id,user_id,v):
    data = v.split(",")
    _url = "http://app.dcinside.com/api/gall_del.php"
    _hd = {
        "User-agent" : "dcinside.app",
        "Referer" : "http://www.dcinside.com"
    }
    _data = {
        "user_id" : user_id,
        "id" : data[1],
        "no" : data[0],
        "mode" : "board_del",
        "app_id" : app_id
    }
    try:
        requests.post(url=_url,headers=_hd,data=_data)
    except:
        sleep(10)




def deletelist(id,pw,lists):
    user_id = getUserid(id,pw)
    app_id = getAppid()
    for v in lists:
        try:
            deletereq(id,app_id,user_id,v)
        except:
            print("차단먹혔습니다 잠시후 10초후 다시실행합니다")
            sleep(10)


def returnlistcnt(list):
    return len(list)

def main(id,pw,boardlist,label):
    label.setText("삭제중...")
    deletelist(id,pw,boardlist)
    onelist = boardlist[int((len(boardlist)/2)):]
    twolist = boardlist[:int((len(boardlist)/2))]
    t1 = threading.Thread(target=deletelist, args=(id,pw,onelist))
    t1.start()
    t2 = threading.Thread(target=deletelist, args=(id,pw,twolist))
    t2.start()