import requests
from bs4 import BeautifulSoup

def appendlist(data,list):
    for v in data['gallog_list']['data']:
        list.append(v['no'])
    return list

def getCSRFtoken(id,cookies,c):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" : cookies
    }

    url = "https://m.dcinside.com/gallog/%s?menu=%s" % (id,c)
    res = requests.get(url=url,headers=_hd)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    csrf = soup.find_all("meta",{"name" : "csrf-token"}) # get csrf token
    return csrf[0].get("content")

def getlist(id,cookies,c):
    returnlist = list()
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
        appendlist(data,returnlist)
        nowPage = "http://m.dcinside.com/gallog/%s?menu=%s&page=%s" %(id,c,page)
        snowPage = "https://m.dcinside.com/gallog/%s?menu=%s&page=%s" %(id,c,page) # last_page_url에서 뱉는값이  https 일때 가정\)
        endPage = data['gallog_list']['last_page_url']
        if((nowPage == endPage) or (snowPage == endPage)):
            break
        else:
            page = page + 1
    return returnlist

def main(id,cookies,num):
    if(num==1):
        commentlist = getlist(id,cookies,"R")
        return commentlist
    elif(num==2):
        postlist = getlist(id,cookies,"G")
        return postlist
    elif(num==3):
        commentlist = getlist(id,cookies,"R")
        postlist = getlist(id,cookies,"G")
        return commentlist, postlist