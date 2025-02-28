import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/s02'
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie' : '__gads=ID=429b88652892e37c:T=1737894287:RT=1737980380:S=ALNI_MYu90UiyZ14N259xJF4i74eyWQqpw; __gpi=UID=0000100f4621342d:T=1737894287:RT=1737980380:S=ALNI_MZtYQQVLwWfK4bfcpZQyV7_ffdC9g; __eoi=ID=6bb051760c1b3d16:T=1737894287:RT=1737980380:S=AA-AfjapWf8S_ZyoeQ3Hya6bO1V0'
}
response = requests.get(url=url,headers=header)
data = response.text

f = open('S02.txt','w',encoding='utf-8')

root = etree.HTML(text=data,parser=None)
trs = root.xpath('//tr')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s += str(td.text) + '|'
    if s != '':
        f.write(s + '\n')            
f.close()        

print('Done')