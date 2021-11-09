import xlrd
import pandas as pd

wb=xlrd.open_workbook("评论数据.xlsx")
sh=wb.sheet_by_index(0)
col=sh.ncols
row=sh.nrows
Text=[]
for i in range(row):
    Text_Context=sh.row_values(i,1,2)[0]
    Text.append(Text_Context)
del Text[0]
print(Text)


#结巴分词
import jieba
import gensim
#停用词处理

import spacy
from spacy.lang.zh.stop_words import STOP_WORDS

sent_words = []
for sent0 in Text:
    try:
        l=list(jieba.cut(sent0))
        # print(l)
        filtered_sentence = []
        for word in l:
            if word not in STOP_WORDS:
                filtered_sentence.append(word)
        sent_words.append(filtered_sentence)
        # print( filtered_sentence)
    except:
        pass
print(sent_words)
document = []

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

tfidf_model = TfidfVectorizer().fit(document)
# 得到语料库所有不重复的词
feature = tfidf_model.get_feature_names()
print(feature)
# 得到每个特征对应的id值：即上面数组的下标
print(tfidf_model.vocabulary_)

# 每一行中的指定特征的tf-idf值：
sparse_result = tfidf_model.transform(document)

# 每一个语料中包含的各个特征值的tf-idf值：
# 每一行代表一个预料，每一列代表这一行代表的语料中包含这个词的tf-idf值，不包含则为空
weight = sparse_result.toarray()

# 构建词与tf-idf的字典：
feature_TFIDF = {}
for i in range(len(weight)):
    for j in range(len(feature)):
        # print(feature[j], weight[i][j])
        if feature[j] not in feature_TFIDF:
            feature_TFIDF[feature[j]] = weight[i][j]
        else:
            feature_TFIDF[feature[j]] = max(feature_TFIDF[feature[j]], weight[i][j])
# print(feature_TFIDF)

# 按值排序：
print('TF-IDF 排名前十的(TF-IDF>1时)：')
featureList = sorted(feature_TFIDF.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
for i in range(10):
    print(featureList[i][0], featureList[i][1])

k=0
m=0
print('TF-IDF 排名前十的(TF-IDF<1时)：')
while k<=10:
    if featureList[m][1]<1:
        k+=1
        print(featureList[m][0], featureList[m][1])
    m+=1

