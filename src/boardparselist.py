import requests
import json
from bs4 import BeautifulSoup
from time import sleep

def getgallname(id,code,csrf): # gall_code를 gall_name으로 변환시키는 function 
    _url = "https://m.dcinside.com/gallog/list-direct"
    _hd = {
        "User-agent" : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G955N Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
        "Referer" : "https://m.dcinside.com/gallog/%s" % (id),
        "X-CSRF-TOKEN" : csrf
    }
    _data =  {
        "gall_code" : code
    }
    req = requests.post(url=_url,headers=_hd,data=_data)
    data = req.json()
    return data["gall_id"]

def appendlist(id,data,list,csrf,gallcodedic):
    for v in data['gallog_list']['data']:
        if v['cid'] in gallcodedic.keys(): # gallcode에 많은요청을보내면 차단을먹어 똑같은값보낼시 딕셔너리참고
            list.append(v['pno']+","+gallcodedic[v['cid']]) # [pno,gall_name] 으로 저장됌
        else:
            gall_name = getgallname(id,v['cid'],csrf)  # gall_code를 gall_name으로 변환
            sleep(1)
            gallcodedic[v['cid']] = gall_name
            list.append(v['pno']+","+gall_name) # [pno,gall_name] 으로 저장됌
        # pno : 게시글 번호
    return list

def getCSRFtoken(id,cookies,c):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" : cookies
    }
    url = "https://m.dcinside.com/gallog/%s/menu=%s" % (id,c)
    res = requests.get(url=url,headers=_hd)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    csrf = soup.find_all("meta",{"name" : "csrf-token"}) # get csrf token
    return csrf[0].get("content")

def getlist(id,cookies,c):
    returnlist = list()
    gallcodedic = dict()
    csrf = getCSRFtoken(id,cookies,c)
    page = 1
    nowPage = "https://m.dcinside.com/gallog/%s?menu=%s&page=1" %(id,c)
    while(1):
        _hd = {
            "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
            "Cookie" :  cookies,
            "Referer" : "https://m.dcinside.com/gallog/%s?menu=%s&page=%s" % (id,c,page),
            "X-TOKEN-CSRF" : csrf,
            "X-Requested-With" : "XMLHttpRequest"
        }
        url = "https://m.dcinside.com/ajax/response-galloglist"
        _payload = {
            "g_id" : id,
            "menu" : c,
            "page" : page,
            "list_more" : "1",
        }
        res = requests.post(url,data=_payload,headers=_hd)
        data = res.json()
        appendlist(id,data,returnlist,csrf,gallcodedic)
        nowPage = "http://m.dcinside.com/gallog/%s?menu=%s&page=%s" %(id,c,page)
        snowPage = "https://m.dcinside.com/gallog/%s?menu=%s&page=%s" %(id,c,page) # last_page_url에서 뱉는값이  https 일때 가정\)
        endPage = data['gallog_list']['last_page_url']
        if((nowPage == endPage) or (snowPage == endPage)):
            break
        else:
            page = page + 1
    return returnlist

def main(id,cookies):
    postlist = getlist(id,cookies,"G_all")
    return postlist