import requests
import json

url = 'https://www.spiderbuf.cn/playground/iplist'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie':'__gads=ID=429b88652892e37c:T=1737894287:RT=1738083722:S=ALNI_MYu90UiyZ14N259xJF4i74eyWQqpw; __gpi=UID=0000100f4621342d:T=1737894287:RT=1738083722:S=ALNI_MZtYQQVLwWfK4bfcpZQyV7_ffdC9g; __eoi=ID=6bb051760c1b3d16:T=1737894287:RT=1738083722:S=AA-AfjapWf8S_ZyoeQ3Hya6bO1V0'
}
response = requests.get(url=url,headers=header)
response.encoding = 'utf-8'
data_json = response.text
data = json.loads(data_json)
f = open('S07.txt','w',encoding='utf-8')
for i in range(11):
    line = data[i-1]
    s = line.values()
    string = ''
    for item in s:
        string = string + item + '|'
    f.write(string + '\n')
f.close()

print('Done')