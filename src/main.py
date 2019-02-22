from login import main as login
from parselist import main as parse

id = input("ID : ")
pw = input("PASS : ")
headers = login(id,pw)
parse(headers)