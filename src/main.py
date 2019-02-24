from login import main as login
from parselist import main as parse
from delete import main as delete
from time import sleep

print("작동이 안될시 프로그래밍갤러리 피에로를 찾아와주세요")
id = input("ID : ")
pw = input("PASS : ")
cookies, id = login(id,pw)
sleep(3)
print("")
print("댓글만 삭제시 1 입력후 엔터")
print("작성글만 삭제시 2 입력후 엔터")
print("둘다 삭제시 3 입력후 엔터")
num = int(input("입력  : "))
print("")
print("수집중입니다 잠시만 기다려주세요")
if(num==1):
    cmtlist = parse(id,cookies,num)
    delete(id,cookies,"R",cmtlist=cmtlist)
elif(num==2):
    pstlist = parse(id,cookies,num)
    delete(id,cookies,"G",pstlist=pstlist)
elif(num==3):
    cmtlist, pstlist = parse(id,cookies,num)
    delete(id,cookies,"R",cmtlist=cmtlist,pstlist=pstlist)
end = input()
