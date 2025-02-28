import jieba
print(jieba.lcut('中华人民共和国是一个伟大的国家'))
print(jieba.lcut('你会不会跳鸡你太美'))
jieba.add_word('鸡你太美')
print(jieba.lcut('你会不会跳鸡你太美'))