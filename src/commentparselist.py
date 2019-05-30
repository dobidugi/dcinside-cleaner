import requests
import json
from time import sleep
from bs4 import BeautifulSoup


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
    print(req.text)
    data = req.json()
    print("\""+code+"\" : \""+data["gall_id"]+"\",")
    return data["gall_id"]
    

def appendlist(id,data,list,csrf,gallcodedic):
    for v in data['gallog_list']['data']:
        if v['cid'] in gallcodedic.keys(): # gallcode에 많은요청을보내면 차단을먹어 똑같은값보낼시 딕셔너리참고
            list.append(v['pno']+","+gallcodedic[v['cid']]+","+v['cno']) # [pno,gall_name,cno] 으로 저장됌
        else:
            gall_name = getgallname(id,v['cid'],csrf)  # gall_code를 gall_name으로 변환
            sleep(3)
            gallcodedic[v['cid']] = gall_name
            list.append(v['pno']+","+gall_name+","+v['cno']) # [pno,gall_name,cno] 으로 저장됌
        # pno = 댓글번호
        # cno = 게시글 번호
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
    gallcodedic = {
    "2489" : "superidea",
    "1290" : "slife",
    "1128" : "kyonggi",
    "2127" : "ncdinos",
    "1029" : "eunuch",
    "7" : "fish",
    "7101" : "tigers_new",
    "1240" : "baseball_ab",
    "4497" : "beard",
    "2928" : "godverfool",
    "463" : "football_k",
    "362" : "game1",
    "2117" : "football_new5",
    "410" : "smile",
    "2220" : "pokemon",
    "2320" : "giants_new1",
    "498" : "book",
    "1668" : "ma9",
    "197" : "movie2",
    "332" : "pop",
    "1506" : "parkboyoung",
    "8602" : "winkgall",
    "1320" : "chicken",
    "1913" : "starcraft_new",
    "2446" : "baseball_new4",
    "6148" : "hobgoblin",
    "346" : "america_ani",
    "283" : "hiphop",
    "543" : "wwe",
    "19931" : "top12",
    "1725" : "jejungwon",
    "601" : "etc_g",
    "7234" : "stock_new2",
    "5437" : "bang_dream",
    "7126" : "epicseven",
    "364" : "fps",
    "19298" : "github",
    "839" : "hit",
    "2343" : "lgbt",
    "169" : "pmp",
    "193" : "room",
    "8599" : "kdani",
    "22257" : "game1_new",
    "7092" : "game_classic1",
    "791" : "sweets",
    "26249" : "baseball_new8",
    "10520" : "drama_new2",
    "596" : "food",
    "6406" : "yourname",
    "4043" : "netflix",
    "1333" : "sweet",
    "1802" : "loan",
    "1624" : "touhou",
    "187" : "dongau",
    "17494" : "doosanbears_new1",
    "2946" : "sunshine",
    "2872" : "r6",
    "2933" : "lostark",
    "17521" : "leagueoflegends2",
    "544" : "rhythmgame",
    "2119" : "comic_new1",
    "62" : "dog",
    "404" : "food_noodle",
    "1634" : "physicalscience",
    "657" : "bike",
    "1967" : "battlefield3",
    "11046" : "brawl",
    "2239" : "bitcoins",
    "147" : "samgugji",
    "17341" : "3017",
    "2741" : "firefighter",
    "3811" : "soulworker",
    "1830" : "exam_new",
    "1716" : "smartphone",
    "210" : "tree",
    "979" : "arbeit",
    "2256" : "idolmaster",
    "519" : "cat",
    "1814" : "elsword",
    "8368" : "mnet_k",
    "3455" : "yjrs",
    "211" : "history",
    "2099" : "worldoftanks",
    "1436" : "army",
    "1248" : "earphone",
    "13905" : "ib_new",
    "2623" : "japan_voice",
    "408" : "pride",
    "6965" : "aoegame",
    "2159" : "shingeki",
    "151" : "train",
    "14869" : "kaguya",
    "216" : "cartoon",
    "1872" : "pridepc_new3",
    "1980" : "comedy_new1",
    "1821" : "tabletpc",
    "237" : "toy",
    "407" : "lotto",
    "744" : "different",
    "2481" : "ff14",
    "649" : "reptile",
    "4634" : "paradox",
    "1804" : "cs",
    "733" : "programming",
    "20918" : "projectgirlgroup",
    "3311" : "pripara",
    "2264" : "hearthstone",
    "1099" : "adexam",
    "263" : "modernwar",
    "2429" : "twice",   
    "1100" : "government",
    "2512" : "granblue",
    "10519" : "m_entertainer1",
    "7100" : "d_fighter_new1",
    "2254" : "lovelive",
    "1510" : "maplestory",
    "2428" : "monsterhunter",
    "262" : "divination",
    "2470" : "depression",
    "2269" : "kancolle",
    "2422" : "typemoon",
    "2100" : "fantasy_new",
    "22771" : "producex",
    "18353" : "football_new6",
    "180" : "extra",
    "8746" : "tmfro",
    "13901" : "etc_program2",
    "6017" : "piyo",
    "17801" : "rome",
    "17501" : "baseball_new7",
    "17313" : "vr",
    "2399" : "akb48",
    "1892" : "pc",
    "1933" : 'wow_new3',
    "39" : "nintendo",
    "619" : "diet",
    "2124" : "anigallers_new",
    "377" : "lotto2",
    "235" : "mystery",
    "239" : "immovables",
    "270" : "announcer2",
    "1976" : "ani1_new1",
    "165" : "English",
    "9308" : "wannaone",
    "3390" : "warframe",
    "4860" : "gfl",
    "2677" : "nogada",
    "15538" : "blnovel",
    "2" : "bicycle",
    "1928" : "jdh",
    "4591" : "fightgametekken",
    "2371" : "closers",
    "6889" : "315pro",
    "12975" : "gotoyome",
    "7126" : "epicseven",
    "20234" : "manjuugame",
    "18701" : "stream",
    "4310" : "grand3chase",
    "5766" : "dbd",
    "6592" : "pebble",
    "22589" : "lastorigin",
    "18845" : "langrisser",
    "6260" : "rimworld",
    "21062" : "stockus",
    "8443" : "theaterdays",
    "13916" : "vespa",
    "17700" : "gfl2",
    "2839" : "jusik",
    "8815" : "arma",
    "19342" : "asiaenter",
    "26859" : "shouta",
    "8725" : "coin",
    "9081" : "soviet",
    "4447" : "pumpitup",
    "1579" : "fight_game",
    "672" : "agony",
    "615" : "fishing",
    "3207" : "r6s",
    "495" : "baduk",
    "1080" : "societyexam",
    "274" : "plastic_ss",
    "1705" : "iphone",
    "2545" : "entertain",
    "2571" : "overwatch",
    "2395" : "got",
    "1092" : "faexam",
    "7309" : "old_game",
    "5804" : "car",
    "2498" : "sc",
    "2162" : "hero2009",
    "1813" : "gongik_new",
    "361" : "game_classic",
    "2391" : "hos",
    "13823" : "baseball_new6",
    "2215" : "baseball_new2",
    "2341" : "baseball_new3",
    "2009" : "baseball_new1",
    "7251" : "baseball_new5",
    "587" : "lineage",
    "2078" : "fashion_new1",
    "1434" : "baram",
    "1843" : "d_fighter_new",
    "2077" : "leagueoflegends1",
    "1885" : "leagueoflegends",
    "1879" : "sundaynight",
    "2438" : "stock_new1",
    "1841" : "news_new",
    "8858" : "female__singer",
    "8819" : "girlgroup",
    "25028" : "dota2autochess",
    "20958" : "johong",
    "12218" : "kawai3",
    "3411" : "ttwar",
    "23968" : "tullius",
    "10917" : "powerlifting",
    "13801" : "mfgo",
    "20510" : "fromis9real",
    "25314" : "purikone_redive",
    "17500" : "hanwhaeagles_new",
    "2381" : "fifaonline",
    "2008" : "doosanbears_new",
    }   
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
        try:
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
        except:
            print("감지")
    return returnlist

def main(id,cookies): 
    commentlist = getlist(id,cookies,"R_all")
    return commentlist