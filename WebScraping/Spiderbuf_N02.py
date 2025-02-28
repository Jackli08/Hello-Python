import requests
import re
import base64

url = 'https://www.spiderbuf.cn/playground/n02'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Referer':'https://www.spiderbuf.cn/web-crawling-examples/2?order=learn'
}
response = requests.get(url=url,headers=header)
html = response.text
data1 = re.findall(r'c="data:image/png;base64,(.*?)" />',html,re.S)[0]
str_bytes = data1.encode('raw_unicode_escape')
data2 = base64.b64decode(str_bytes)
f = open('N02.png','wb')
f.write(data2)
f.close()

print('Done')