from login import main as login
from parselist import main as parse
from delete import main as delete

print("작동이 안될시 프로그래밍갤러리 피에로를 찾아와주세요")
id = input("ID : ")
pw = input("PASS : ")
cookies, id = login(id,pw)
print("댓글만 삭제시 1 입력후 엔터")
print("작성글만 삭제시 2 입력후 엔터")
print("둘다 삭제시 3 입력후 엔터")
num = int(input())
if(num==1):
    cmtlist = parse(id,cookies,num)
elif(num==2):
    pstlist = parse(id,cookies,num)
elif(num==3):
    cmtlist, pstlist = parse(id,cookies,num)
