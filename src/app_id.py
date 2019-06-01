import requests
import json
import hashlib
from datetime import datetime

def hashValueToken():
    now = datetime.now()
    str1 = "dcArdchk_%04d%02d%02d%02d" % (now.year,now.month,now.day,now.hour)
    data = hashlib.sha256(str1.encode()).hexdigest()
    return data

def main():
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