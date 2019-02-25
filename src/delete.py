import requests
import json
from bs4 import BeautifulSoup
from time import sleep

def getCSRFtoken(id,cookies,c):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" : cookies,
        "Referer" : "https://m.dcinside.com/gallog/%s?menu=%s" % (id,c),
    }

    url = "http://m.dcinside.com/gallog/%s?menu=%s" % (id,c)
    res = requests.get(url=url,headers=_hd)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    csrf = soup.find_all("meta",{"name" : "csrf-token"}) # get csrf token
    return csrf[0].get("content")

def getBlockKey(id,cookies,csrf,c):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "https://m.dcinside.com/gallog/%s?menu=%s" % (id,c),
        "X-CSRF-TOKEN" : csrf,
        "X-Requested-With" : "XMLHttpRequest",
        "Cookie" : cookies,
    }
    _payload = {
        "token_verify" : "gallogDel"
    }

    url = "https://m.dcinside.com/ajax/access"
    res = requests.post(url,data=_payload,headers=_hd)
    data = res.json()
    return data['Block_key']

def deletereq(id,cookies,block_key,csrf,v,c,CountDel,AllCount):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "https://m.dcinside.com/gallog/%s?menu=%s" % (id,c),
        "X-CSRF-TOKEN" : csrf,
        "X-Requested-With" : "XMLHttpRequest",
        "Cookie" : cookies + "m_dcinside_lately=programming;m_gallog_lately=%s;m_gallog_%s=%s" % (id,id,id)
    }
    _payload = {
        "con_key" : block_key,
        "g_id" : id,
        "no" : v   
    }

    url = "https://m.dcinside.com/gallog/log-del"
    requests.post(url,data=_payload,headers=_hd)
    print("%d / %d" %(CountDel,AllCount))
    CountDel = CountDel + 1


def deletelist(id,cookies,lists,c,CountDel=0,AllCount=0):
    AllCount = len(lists)
    for v in lists:
        CountDel = CountDel + 1 
        csrf = getCSRFtoken(id,cookies,c)
        block_key = getBlockKey(id,cookies,csrf,c)
        try:
            deletereq(id,cookies,block_key,csrf,v,c,CountDel,AllCount)
        except:
            print("차단방지를위해 위해 30초후 자동재시작됩니다.")
            sleep(30)
            try:
                deletereq(id,cookies,block_key,csrf,v,c,CountDel,AllCount)
            except:
                print("차단방지를위해 위해 30초후 자동재시작됩니다.")
                sleep(30)
                deletereq(id,cookies,block_key,csrf,v,c,CountDel,AllCount)
    CountDel = 0
    AllCount = 0 

def askstart():
    print("")
    print("작업을 진행하시려면 1번을 입력후 엔터를 눌러주세요")
    print("작업을 진행하지않으려면 2번을 입력후 엔터를 눌러주세요")
    answer = int(input("입력 : "))
    print("")
    print("작업이 시작됬습니다 잠시만 기다려주세요")
    if(answer==2):
        exit(1)

def endtalk():
    print("")
    print("요청하신 작업이 모두 끝났습니다")
    print("남아있는 글이나 댓글이 있을시 다시한번 돌려주세요")

def returnlistcnt(list):
    return len(list)

def main(id,cookies,c,cmtlist="",pstlist=""):
    print("수집이 완료되었습니다")
    print("갯수가 맞지않는다면 작업진행후 한번더다시 반복해주세요")
    if(pstlist==""):
        print("총 댓글 갯수 : %d" % returnlistcnt(cmtlist))
        askstart()
        print("댓글삭제시작")
        deletelist(id,cookies,cmtlist,c,0,0)
        endtalk()
    elif(cmtlist==""):
        print("총 작성글 갯수 : %d" % returnlistcnt(pstlist))
        askstart()
        print("작성글삭제시작")
        deletelist(id,cookies,pstlist,c,0,0)
        endtalk()
    else:
        print("총 댓글 갯수 : %d" % returnlistcnt(cmtlist))
        print("총 작성글 갯수 : %d" % returnlistcnt(pstlist))
        askstart()
        print("댓글삭제시작")
        deletelist(id,cookies,cmtlist,c,0,0)
        c="G"
        print("")
        print("작성글삭제시작")
        deletelist(id,cookies,pstlist,c)
        endtalk()