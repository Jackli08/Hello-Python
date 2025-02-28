import requests
from lxml import etree
from time import sleep

base_url = 'https://www.spiderbuf.cn/playground/n03/2'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
base_response = requests.get(url=base_url,headers=header)
base_html = base_response.text
base_root = etree.HTML(text=base_html,parser=None)
sleep(1)
f = open('N03.txt','a',encoding='utf-8')
for i in range(1,21):
    url = 'https://www.spiderbuf.cn' + base_root.xpath('/html/body/main/div[2]/div/div/div/nav/ul/li[{}]/a/@href'.format(i + 1))[0]
    response = requests.get(url=url,headers=header)
    html = response.text
    root = etree.HTML(text=html,parser=None)
    trs = root.xpath('//tr')
    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.text) + '|'
        if s != '':
            f.write(s + '\n')
    sleep(1)
f.close()

print('Done')