import requests
import json
from bs4 import BeautifulSoup



def getCSRFtoken():
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }

    url = "http://m.dcinside.com/auth/login"
    req = requests.get(url=url,headers=_hd)
    html = req.text
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
    req = requests.post(url,headers=_hd,data=_payload)
    data = req.json()
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
    req = requests.post(url,headers=_hd,data=_payload)
    return req.headers["Set-Cookie"]

def main(id,password):
    csrf = getCSRFtoken()
    block_key = getBlockKey(csrf)
    headers = login(id,password,block_key)
    return headers