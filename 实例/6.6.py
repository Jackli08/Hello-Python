import jieba
excludes = ['什么','一个','我们','那里','你们','如今','说道','知道','姑娘','这里','起来',\
'出来','他们']
txt = open('红楼梦.txt','r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))