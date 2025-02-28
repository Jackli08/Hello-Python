import requests
from lxml import etree

base_url = 'https://www.spiderbuf.cn/playground/e04/2fe6286a4e5f'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie':'__gads=ID=429b88652892e37c:T=1737894287:RT=1738083722:S=ALNI_MYu90UiyZ14N259xJF4i74eyWQqpw; __gpi=UID=0000100f4621342d:T=1737894287:RT=1738083722:S=ALNI_MZtYQQVLwWfK4bfcpZQyV7_ffdC9g; __eoi=ID=6bb051760c1b3d16:T=1737894287:RT=1738083722:S=AA-AfjapWf8S_ZyoeQ3Hya6bO1V0'
}
responses = requests.get(url=base_url,headers=header)
html_datas = responses.text
roots = etree.HTML(text=html_datas,parser=None)
f = open('E04.txt','a',encoding='utf-8')
for i in range(2,7):
    url = 'https://www.spiderbuf.cn' + str(roots.xpath('/html/body/main/div[2]/div/nav/ul/li[{}]/a/@href'.format(i))[0])
    response = requests.get(url=url,headers=header)
    html_data = response.text
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