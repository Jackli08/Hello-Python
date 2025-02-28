import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/e02/list'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie':'admin=fdfbfe8d2a25ab4822e820ea51420cb5'
}
payload = {'username':'admin','password':'123456'}
response = requests.get(url=url,headers=header,data=payload)
html_data = response.text
f = open('E02.txt','w',encoding='utf-8')
root = etree.HTML(text=html_data,parser=None)
trs = root.xpath('//tr')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    if s != '':
        f.write(s + '\n')
f.close()

print('Done')