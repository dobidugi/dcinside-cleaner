import requests
import json
from bs4 import BeautifulSoup

def getCSRFtoken():
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }

    url = "https://m.dcinside.com/auth/login?r_url=https%3A%2F%2Fm.dcinside.com"
    req = requests.get(url=url,headers=_hd)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    csrf = soup.find_all("meta",{"name" : "csrf-token"}) # get csrf token
    return csrf[0].get("content")

def getBlockKey(csrf):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "https://m.dcinside.com/auth/login?r_url=https%3A%2F%2Fm.dcinside.com",
        "X-CSRF-TOKEN" : csrf,
        "X-Requested-With" : "XMLHttpRequest"
    }
    _payload = {
        "token_verify" : "dc_login",
        "con_key" : csrf
    }

    url = "https://m.dcinside.com/ajax/access"
    req = requests.post(url=url,headers=_hd)
    data = req.json()
    return data['Block_key']
    
def login(id,pw,block_key):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Referer" : "https://m.dcinside.com/auth/login?r_url=https%3A%2F%2Fm.dcinside.com",
        "Upgrade-Insecure-Requests" : "1"
    }
    _payload = {
        "user_id" : id,
        "user_pw" : pw,
        "id_chk" : "on",
        "con_key" : block_key,
        "r_url" : "https://m.dcinside.com"
    }
    _cookie = {
        "PHPSESSID" : "f4c886bc4551e72c1ace62c2d95ef580"
    }
    url = "https://dcid.dcinside.com/join/mobile_login_ok_new.php"
    req = requests.post(url=url,headers=_hd,data=_payload,cookies=_cookie)
    print(req.headers["Date"])

def gogall(cookie):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" : "PHPSHESSID="+cookie
    }

    url = "http://gallog.dcinside.com/fakemarine"
    req = requests.get(url=url,headers=_hd)
    print(req.text)

def main(id,password):
    csrf = getCSRFtoken()
    block_key = getBlockKey(csrf)
    login(id,password,block_key)
    #gogall(cookie)


