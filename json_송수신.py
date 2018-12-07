import json
import urllib.request

url = "http://ip.jsontest.com"  # URL

f = open("C:/Python/exam-src/sample.json",'r')

#전체파일 Read
d = f.read()
f.close()

params = json.dumps(d).encode("utf-8")
req = urllib.request.Request(url, data=params, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))  # decode: 바이트를 문자열로 변환

#while True:
#    line = f.readline()
#    if not line: break


