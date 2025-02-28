import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/n01'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'referer':'https://www.spiderbuf.cn/web-crawling-examples/2?order=learn'
}
response = requests.get(url=url,headers=header)
html_data = response.text
f = open('N01.txt','a',encoding='utf-8')
root = etree.HTML(text=html_data,parser=None)
ls = root.xpath('//div[@class ="container"]/div/div')
for item in ls:
    name = item.xpath('./h2')[0].text
    datas = item.xpath('./p')
    data_1 = datas[0].text
    data_2 = datas[1].text
    data_3 = datas[2].text
    data_4 = datas[3].text
    s = ''
    s = s + name + '|' + data_1.replace('排名：','') + '|' + data_2.replace('企业估值(亿元)：','') + '|' + data_3.replace('CEO：','') + '|' + data_4.replace('行业：','')
    if s != '':
        f.write(s + '\n')
f.close()

print('Done')