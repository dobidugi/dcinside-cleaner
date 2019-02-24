import requests
from bs4 import BeautifulSoup
from time import sleep

def appendlist(tag,list):
    for v in tag:
        list.append(v.get("no"))
    return list

def getcommentlist(id,cookies):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" :  cookies
    }
    commentlist = list()
    page=1
    while True:
        sleep(0.05)
        url = "http://m.dcinside.com/gallog/%s?menu=R&page=%d" %(id,page)
        res = requests.get(url,headers=_hd)
        html = res.text
        soup = BeautifulSoup(html,"lxml")
        tag  = soup.find_all("a",{"class" : "del-rt"})
        if not tag:
            break
        commentlist = appendlist(tag,commentlist)
        page = page + 1
    return commentlist

def getpostlist(id,cookies):
    _hd = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36",
        "Cookie" :  cookies
    }
    postlist = list()
    page=1
    while True:
        sleep(0.03)
        url = "http://m.dcinside.com/gallog/%s?menu=G&page=%d" %(id,page)
        res = requests.get(url,headers=_hd,timeout=3)
        html = res.text
        soup = BeautifulSoup(html,"lxml")
        tag  = soup.find_all("a",{"class" : "del-rt"})
        if not tag:
            break
        postlist = appendlist(tag,postlist)
        page = page + 1
    return postlist
    
def main(id,cookies,num):
    if(num==1):
        commentlist = getcommentlist(id,cookies)
        return commentlist
    elif(num==2):
        postlist = getpostlist(id,cookies)
        return postlist
    elif(num==3):
        commentlist = getcommentlist(id,cookies)
        postlist = getpostlist(id,cookies)
        return commentlist, postlist