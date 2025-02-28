import requests
from lxml import etree

url = 'https://www.spiderbuf.cn/playground/n04'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=header)
html = response.text
root = etree.HTML(text=html,parser=None)
dic = {'abcdef::before':7,'abcdef::after':5,'ghijkl::before':8,'ghijkl::after':9,'mnopqr::before':9,'mnopqr::after':1,'uvwxyz::before':1,'uvwxyz::after':4,'yzabcd::before':2,'yzabcd::after':6,'efghij::before':3,
'efghij::after':2,'klmnop::before':5,'klmnop::after':7,'qrstuv::before':4,'qrstuv::after':3,'wxyzab::before':6,'wxyzab::after':0,'cdefgh::before':0,'cdefgh::after':8,'hijklm::after':6,'opqrst::after':0,'uvwxab::after':3,
'cdijkl::after':8,'pqrmno::after':1,'stuvwx::after':4,'pkenmc::after':7,'tcwdsk::after':9,'mkrtyu::after':5,'umdrtk::after':2}
# '豆瓣电影评分:'
f = open('N04.txt','a',encoding='utf-8')
for i in range(2,12):
    try:
        name = root.xpath('/html/body/div[2]/div[{}]/div/h2'.format(i))[0].text
        old_rate = root.xpath('/html/body/div[2]/div[{}]/div/div[2]/span[2]/@class'.format(i))[0]
        old_list = old_rate.split(' ')
        char1 = dic.get(old_list[0] + '::before')
        char2 = dic.get(old_list[1] + '::after')
        rate = str(char1) + '.' + str(char2)
        s = ''
        s = s + name + ' ' + '豆瓣电影评分:' + rate
        if s != '':
            f.write(s + '\n')
    except:
        continue
f.close()

print('Done')

# /html/body/div[2]/div[2]/div/div[2]/span[2]
# /html/body/div[2]/div[3]/div/div[2]/span[2]
# /html/body/div[2]/div[5]/div/div[2]/span[2]
# /html/body/div[2]/div[7]/div/div[2]/span[2]
# /html/body/div[2]/div[9]/div/div[2]/span[2]
# /html/body/div[2]/div[11]/div/div[2]/span[2]