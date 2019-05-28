from login import main as login
from parselist import main as parse
from delete import main as delete
from divparselist import main as divparse
from time import sleep


def ProcessSelect():
    print("========================================")
    print("원하시는 작업을 선택하고 엔터를 눌러주세요")
    print("1. 댓글만 삭제하기")
    print("2. 작성글만 삭제하기")
    print("3. 댓글,작성글 삭제하기")
    num = int(input("입력  : "))
    print("========================================")
    print("수집중입니다 잠시만 기다려주세요")
    return num

def NormalDel():
    num = ProcessSelect()
    if(num==1):
        cmtlist = parse(id,cookies,num)
        #delete(id,cookies,"R",cmtlist=cmtlist)
    elif(num==2):
        pstlist = parse(id,cookies,num)
        #delete(id,cookies,"G",pstlist=pstlist)

    elif(num==3):
        cmtlist, pstlist = parse(id,cookies,num)
        #delete(id,cookies,"R",cmtlist=cmtlist,pstlist=pstlist)


# programe start
print("작동이 안될시 프로그래밍갤러리 피에로를 찾아와주시거나")
print("dobidugi@gmail.com 이쪽으로 증상과 메일을 보내주세요^^")
id = input("ID : ")
pw = input("PASS : ")
cookies, id = login(id,pw)
NormalDel()
