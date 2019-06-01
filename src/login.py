import requests
import json
from bs4 import BeautifulSoup
from time import sleep

def getCSRFtoken():
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }

    url = "http://m.dcinside.com/auth/login"
    res = requests.get(url=url,headers=_hd)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    csrf = soup.find_all("meta",{"name" : "csrf-token"}) # get csrf token
    return csrf[0].get("content")

def getBlockKey(csrf):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "http://m.dcinside.com/auth/login?r_url=http%3A%2F%2Fm.dcinside.com&mode=&rucode=1",
        "X-CSRF-TOKEN" : csrf,
        "X-Requested-With" : "XMLHttpRequest"
    }
    _payload = {
        "token_verify" : "dc_login",
        "con_key" : csrf
    }

    url = "https://m.dcinside.com/ajax/access"
    res = requests.post(url,headers=_hd,data=_payload)
    data = res.json()
    return data['Block_key']
    
def login(id,pw,block_key,suslabel,wrlabel):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "http://m.dcinside.com/auth/login?r_url=http%3A%2F%2Fm.dcinside.com"
    }
    _payload = {
        "user_id": id,
        "user_pw": pw,
        "id_chk": "on",
        "con_key": block_key,
        "r_url": "http://m.dcinsidsse.com/" 
    }
    url = "https://dcid.dcinside.com/join/mobile_login_ok_new.php"
    res = requests.post(url,headers=_hd,data=_payload)
    re = loginchk(res,block_key,suslabel,wrlabel)
    if re == True:
        return res.headers["Set-Cookie"]
    elif re == False:
        return False

def loginchk(res,block_key,suslabel,wrlabel):
    if(len(res.text) == 226):
        suslabel.setText("사용하기전 공앱은 꼭 종료해주세요!")
        wrlabel.setText(" ")
        return True
    else:
        wrlabel.setText("아이디 패스워드를 다시 확인해주세요")
        return False

def main(id,password,suslabel,wrlabel):
    csrf = getCSRFtoken()
    block_key = getBlockKey(csrf)
    cookies = login(id,password,block_key,suslabel,wrlabel)
    return cookies, id