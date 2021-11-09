from sklearn.feature_extraction.text import CountVectorizer

def base_doc():
    from pathlib import Path
    all_txt_files = []
    for file in Path("Foreign_CSR_txt").rglob("*.txt"):
        all_txt_files.append(file.parent / file.name)
    n_files = len(all_txt_files)
    print(n_files)
    all_txt_files.sort()
    for txt_file in all_txt_files:
        with open(txt_file) as f:
            txt_file_as_string = f.read()
        corpus.append(txt_file_as_string)
    print(corpus)


if __name__ == "__main__":

    # 存储读取语料 一行预料为一个文档
    corpus = []
    base_doc()

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    print(vectorizer)

    X = vectorizer.fit_transform(corpus)
    analyze = vectorizer.build_analyzer()
    weight = X.toarray()

    print(len(weight))
    print (weight[:5, :5])

    # LDA算法
    print('LDA:')
    import numpy as np
    import lda
    import lda.datasets

    # 定义主题数量
    n_topics = 10
    # 定义迭代次数
    n_iter = 500
    model = lda.LDA(n_topics=n_topics, n_iter=n_iter, random_state=1)
    model.fit(np.asarray(weight))  # model.fit_transform(X) is also available
    # 主题-单词（topic-word）分布
    topic_word = model.topic_word_  # model.components_ also works

    # 文档-主题（Document-Topic）分布
    doc_topic = model.doc_topic_
    print("type(doc_topic): {}".format(type(doc_topic)))
    print("shape: {}".format(doc_topic.shape))

    # 输出前10篇文章最可能的Topic
    label = []
    for n in range(10):
        topic_most_pr = doc_topic[n].argmax()
        label.append(topic_most_pr)
        print("doc: {} topic: {}".format(n, topic_most_pr))