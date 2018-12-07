from lxml import etree
 
# Empty array
members = []
albums = []
 
# Load XML
tree = etree.parse("sample.xml")
root = tree.getroot()
 
# Get data
kids = root.getchildren()
 
for child in kids:
    if child.tag == "name":
        gname = child.text
    elif child.tag == "members":
        for x_member in child:
            members.append(x_member.text)
    elif child.tag == "albums":
        for x_album in child:
            albums.append([x_album.get("order"), x_album.text])
 
# Print
print("걸그룹 %s에 대한 정보는 다음과 같습니다:" % gname, end="\n\n")
 
print(" 멤버: ", end="")
for index, member in enumerate(members):
    if index > 0: print(", ", end="")
    print(member, end="")
 
print("\n\n [앨범 목록]")
for album in albums:
    print("  * %s: %s" % (album[0], album[1]) )
