import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/n07'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests .get(url=url,headers=headers)
html = response.text
f = open('N07.txt','a',encoding='utf-8')
root = etree.HTML(text=html,parser=None)
divs = root.xpath('/html/body/main/div[2]/div')[2:]
for div in divs:
    s = ''
    s = s + str(div.text)
    if s != '':
        f.write(s + '\n')

print('Done')