import requests
import json
from bs4 import BeautifulSoup

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
    
def login(id,pw,block_key):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
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
    loginchk(res,block_key)
    return res.headers["Set-Cookie"]

def loginchk(res,block_key):
    if(len(res.text) == 226):
        print("로그인 성공")
    else:
        print("아이디 또는 비밀번호를 다시한번 확인해주세요.")
        print("5회이상 오류시 홈페이지에서 직접 풀어주셔야합니다.")
        id = input("ID : ")
        pw = input("PASS : ")
        main(id,pw)

def main(id,password):
    csrf = getCSRFtoken()
    block_key = getBlockKey(csrf)
    cookies = login(id,password,block_key)
    return cookies