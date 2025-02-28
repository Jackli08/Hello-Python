import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/n05'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=header)
dictionary = {'uvwxyz':3,'cdefgh':9,'abcdef':0,'klmnop':6,'mnopqr':2,'yzabcd':4,'wxyzab':8,'efghij':5,'ghijkl':1,}
f = open('N05.txt','a',encoding='utf-8')
html = response.text
root = etree.HTML(text=html,parser=None)
divs = root.xpath('/html/body/main/div[2]/div[2]/div/div')
for div in divs:
    name = div.xpath('./h2')[0].text
    ranking = div.xpath('./p[1]')[0].text
    nums = div.xpath('./p[2]/span/@class')
    s = ''
    for num in nums:
        num = num.split(' ')[-1]
        char = dictionary.get(num)
        s = s + str(char)
    ceo = div.xpath('./p[3]')[0].text
    industry = div.xpath('./p[4]')[0].text
    string = name + '|' + '企业估值(亿元)：' + s + '|' + ceo + '|' + industry
    if string != '':
        f.write(string + '\n')
f.close()

print('Done')