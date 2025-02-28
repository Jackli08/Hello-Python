import requests
import re

url = 'http://spiderbuf.cn/playground/s05'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
html_data = response.text
data = re.findall('<img src="(.*?)" class="img-responsive img-thumbnail"',html_data)
for item in data:
    lists = item.split('/')
    name = lists[-1]
    urls = 'http://spiderbuf.cn' + item
    header = headers
    img_data = requests.get(url=urls,headers=header).content
    img = open(name,'wb')
    img.write(img_data)
    img.close()

print('Done')