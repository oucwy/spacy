# spaCy  NLP 自然语言文本处理库测试，NLTK也是一种。
# Author: markwy@126.com
# History:  2021.2.22 created.

# https://spacy.io/usage/

# pip install -U spacy
# python -m spacy info 查看spacy版本，当前是3.0.0

# 需安装语言模型库：en_core_web_sm （en表示法已废弃）。
# 此处以英语为例，https://spacy.io有中文库
# 语言库：
# 参考了 https://zhuanlan.zhihu.com/p/56725151 
#   注意要把里面下载文件的版本从2.0.0改为3.0.0，否则报兼容错误
# 下载：
#   https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz下载并按安装
# 查语言库对应的spaCy版本:
#   https://github.com/explosion/spacy-models/blob/master/compatibility.json
# 安装：
#   pip install en_core_web_sm-3.0.0.tar.gz

# 运行本程序结果：
# spaCy
# is
# a
# NPL
# processor
# lib
# 完成分词


import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp(u'spaCy is a NPL processor lib.')

for token in doc:
    print(token)