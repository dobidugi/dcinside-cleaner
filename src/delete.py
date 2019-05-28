import requests
import json
import hashlib
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

def getVersion():
    _url = "http://json2.dcinside.com/json0/app_check_A_rina.php"
    _hd  = {
    "User-agent" : "dcinside.app",
    "Referer" : "http://www.dcinside.com"
    }
    req = requests.get(url=_url,headers=_hd)
    data = req.json()
    return data[0]['ver']

def hashValueToken():
    now = datetime.now()
    str1 = "dcArdchk_%04d%02d%02d%02d" % (now.year,now.month,now.day,now.hour)
    data = hashlib.sha256(str1.encode()).hexdigest()
    return data

def getAppid():
    value_token = hashValueToken()
    version = getVersion()
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
    "vName" : version
    }

    req = requests.post(url=_url,headers=_hd,data=_data)
    data = req.json()
    return data[0]["app_id"]



def deletereq(id,app_id,user_id,v,c,CountDel,AllCount):
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
        "mode" : c,
        "app_id" : app_id
    }
    requests.post(url=_url,headers=_hd,data=_data)
    print("%d / %d" %(CountDel,AllCount))
    CountDel = CountDel + 1


def deletelist(id,pw,lists,c,CountDel=0,AllCount=0):
    AllCount = len(lists)
    user_id = getUserid(id,pw)
    app_id = getAppid()
    for v in lists:
        CountDel = CountDel + 1 
        try:
            deletereq(id,app_id,user_id,v,c,CountDel,AllCount)
        except:
            print("차단먹혔습니다 잠시후 10초후 다시실행합니다")
            sleep(10)
    CountDel = 0
    AllCount = 0 

def askstart():
    print("========================================")
    print("작업을 진행할까요?")
    print("I 진행")
    print("II 취소")
    answer = int(input("입력 : "))
    print("")
    print("작업이 시작됬습니다 잠시만 기다려주세요")
    print("========================================")
    if(answer==2):
        exit(0)

def endtalk():
    print("========================================")
    print("요청하신 작업이 모두 끝났습니다")
    print("남아있는 글이나 댓글이 있을시 다시한번 돌려주세요")
    print("1. 프로그램종료")
    print("2. 추가진행")
    sel = int(input("입력  : "))
    print("========================================")
    if(sel == 1 ):
        exit(0)

def returnlistcnt(list):
    return len(list)

def main(id,pw,c,cmtlist="",pstlist=""):
    print("수집이 완료되었습니다")
    print("갯수가 맞지않는다면 작업진행후 한번더다시 반복해주세요")
    if(pstlist==""):
        print("총 댓글 갯수 : %d" % returnlistcnt(cmtlist))
        askstart()
        print("댓글삭제시작")
        deletelist(id,pw,cmtlist,c,0,0)
        endtalk()
    elif(cmtlist==""):
        print("총 작성글 갯수 : %d" % returnlistcnt(pstlist))
        askstart()
        print("작성글삭제시작")
        deletelist(id,pw,pstlist,c,0,0)
        endtalk()
    else:
        print("총 댓글 갯수 : %d" % returnlistcnt(cmtlist))
        print("총 작성글 갯수 : %d" % returnlistcnt(pstlist))
        askstart()
        print("댓글삭제시작")
        deletelist(id,pw,cmtlist,c,0,0)
        print("")
        print("작성글삭제시작")
        deletelist(id,pw,pstlist,c,0,0)
        endtalk()