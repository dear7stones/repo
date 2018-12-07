import json
from collections import OrderedDict
#from pprint import pprint
 
with open('grilfriend.json', encoding="utf-8") as data_file:    
    data = json.load(data_file, object_pairs_hook=OrderedDict)
 
# Print
print("걸그룹 %s에 대한 정보는 다음과 같습니다:" % data["name"], end="\n\n")
 
print(" 멤버: ", end="")
for index, member in enumerate(data["members"]):
    if index > 0: print(", ", end="")
    print(member, end="")
  
print("\n\n [앨범 목록]")
for album, title in data["albums"].items():
    print("  * %s: %s" % (album, title) )
 
#pprint(data)
