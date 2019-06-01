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

def deletereq(id,app_id,user_id,v):
    data = v.split(",")
    _url = "http://m.dcinside.com/api/comment_del.php"
    _hd = {
        "User-agent" : "dcinside.app",
        "Referer" : "http://www.dcinside.com"
    }
    _data = {
        "user_id" : user_id,
        "id" : data[1],
        "no" : data[0],
        "comment_no" : data[2],
        "mode" : "comment_del",
        "app_id" : app_id,
    }
    try:
        req = requests.post(url=_url,headers=_hd,data=_data)
        print(req.text)
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

def main(id,pw,commentlist,label,app_id):
    print(app_id)
    label.setText("삭제중...")
    onelist = commentlist[int((len(commentlist)/2)):]
    twolist = commentlist[:int((len(commentlist)/2))]
    t1 = threading.Thread(target=deletelist, args=(id,pw,onelist,app_id))
    t1.start()
    t2 = threading.Thread(target=deletelist, args=(id,pw,twolist,app_id))
    t2.start()
    label.setText("댓글 삭제 완료!")