import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/s08'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie':'__gads=ID=429b88652892e37c:T=1737894287:RT=1738083722:S=ALNI_MYu90UiyZ14N259xJF4i74eyWQqpw; __gpi=UID=0000100f4621342d:T=1737894287:RT=1738083722:S=ALNI_MZtYQQVLwWfK4bfcpZQyV7_ffdC9g; __eoi=ID=6bb051760c1b3d16:T=1737894287:RT=1738083722:S=AA-AfjapWf8S_ZyoeQ3Hya6bO1V0'
}
payload = {'level':'8'}
response = requests.post(url=url,headers=header,data=payload)
html_data = response.text
f = open('S08.txt','w',encoding='utf-8')
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