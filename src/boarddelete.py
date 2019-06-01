import requests
import json
import threading
from bs4 import BeautifulSoup
from time import sleep

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




def deletelist(id,pw,lists,app_id):
    user_id = getUserid(id,pw)
    for v in lists:
        try:
            sleep(0.5)
            deletereq(id,app_id,user_id,v)
        except:
            print("차단먹혔습니다 잠시후 10초후 다시실행합니다")
            sleep(10)


def returnlistcnt(list):
    return len(list)

def main(id,pw,boardlist,label,app_id):
    print(app_id)
    label.setText("삭제중...")
    onelist = boardlist[int((len(boardlist)/2)):]
    twolist = boardlist[:int((len(boardlist)/2))]
    t1 = threading.Thread(target=deletelist, args=(id,pw,onelist,app_id))
    t1.start()
    t2 = threading.Thread(target=deletelist, args=(id,pw,twolist,app_id))
    t2.start()