# spaCy测试。  spaCy是 NLP 自然语言文本处理库，NLTK也是一种。
# Author: markwy@126.com
# History:  2021.2.22 created.

# https://spacy.io/usage/

# pip install -U spacy
# python -m spacy info 查看spacy版本，当前默认安装的是3.0.0

# 需安装语言模型库：en_core_web_sm （en表示法已废弃）。
# 此处以英语为例，https://spacy.io有中文库
# 语言库：
# 参考了 https://zhuanlan.zhihu.com/p/56725151 
#   
# 下载（注意要把里面下载文件的版本从2.0.0改为3.0.0，否则运行时报兼容错误）：
#   https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz下载并按安装
# 查语言库对应的spaCy版本:
#   https://github.com/explosion/spacy-models/blob/master/compatibility.json
# 安装：
#   pip install en_core_web_sm-3.0.0.tar.gz
# 参考：https://www.cnblogs.com/panchuangai/p/13695902.html


import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp(u"bitcoin is a kind of digital currency not issued by any goverment. It's price reaches $58,000 in February 2021. ")

for token in doc:
    print(token)                        # 分词
    print(token.text, "--", token.pos_) # 标注词性

for ent in doc.ents:
    print(ent.text, ent.label_)         # 标注实体
