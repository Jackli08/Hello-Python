import requests
from lxml import etree

def get_html():
    url = 'https://www.spiderbuf.cn/playground/n06'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    html = response.text
    global f
    f = open('N06.txt','a',encoding='utf-8')
    global root
    root = etree.HTML(text=html,parser=None)

def get_inputs():
    tag_inputs = root.xpath('//input')
    for tag_input in tag_inputs:
        attr_name = tag_input.attrib['name'] if 'name' in tag_input.attrib else ''
        attr_value = ''
        if attr_name != 'gender' and attr_name != 'interest':
            attr_value = attr_value = tag_input.attrib['value'] if 'value' in tag_input.attrib else ''
        if attr_name == 'gender':
            attr_bool = tag_input.attrib['checked'] if 'checked' in tag_input.attrib else ''
            if attr_bool != '':
                attr_value = tag_input.attrib['value'] if 'value' in tag_input.attrib else ''
        if attr_name == 'interest':
            attr_bool = tag_input.attrib['checked'] if 'checked' in tag_input.attrib else ''
            if attr_bool != '':
                attr_value = tag_input.attrib['value'] if 'value' in tag_input.attrib else ''
        if attr_value != '':
            attr_string = attr_name + ':' + attr_value
            f.write(attr_string + '\n')

def get_text():
    text_area = root.xpath('//*[@id="textarea"]')[0].text
    f.write('textarea' + ':' + text_area + '\n')

def get_option():
    options = root.xpath('//option')
    dictionary = {'Monkey.D.Luffy':'蒙奇·D·路飞','Roronoa Zoro':'罗罗诺亚·索隆','Nami':'娜美','Usopp':'乌索普','Sanji':'山治','Tony Tony Chopper':'托尼托尼·乔巴','Nico Robin':'妮可·罗宾','FRANKY':'弗兰奇','BROOK':'布鲁克','Jinbe':'甚平','Silvers Rayleigh':'西尔巴兹·雷利'}
    for option in options:
        attr_bool = option.attrib['selected'] if 'selected' in option.attrib else ''
        if attr_bool != '':
            attr_value = option.attrib['value'] if 'value' in option.attrib else ''
            value = dictionary.get(attr_value)
            f.write('character representative'+ ':' + str(value) + '\n')

def source():
    lis = root.xpath('/html/body/main/div[2]/div/form/div[15]/ul/li')
    for li in lis:
        a = li.xpath('./a')[0]
        attr_bool = a.attrib['class'] if 'class' in a.attrib else ''
        if attr_bool != '':
            if 'active' in attr_bool:
                value = 'source of character representation' + ':' + a.text
                f.write(value + '\n')

def main():
    get_html()
    get_inputs()
    get_text()
    get_option()
    source()
    f.close()

main()

print('Done')