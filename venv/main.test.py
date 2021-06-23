import jieba

# 读取红楼梦的文本内容
txt = open('红楼梦.txt', 'r', encoding='utf-8').read()
# 运用jieba库对文本内容进行分词
words = jieba.lcut(txt)
# 初始化count字典 用于存放人名出现频率
counts = {}
# 读取红楼梦人名信息
names = open('人名.txt', 'r', encoding='utf-8').read().split('、')
# 对分词数据进行筛选 将不需要的数据跳过  只保存有效数据
for word in words:
    if len(word) == 1:
        continue
    elif word == '贾母' or word == '老太太':
        word = '贾母'
    elif word in '贾珍—尤氏'.split('—'):
        word = '贾珍'
    elif word in '贾蓉—秦可卿'.split('-'):
        word = '贾蓉'
    elif word in '贾赦—邢夫人'.split('-'):
        word = '贾赦'
    elif word in '贾政—王夫人'.split('-'):
        word = '贾政'
    elif word in '袭人-蕊珠'.split('-'):
        word = '袭人'
    elif word in '贾琏—王熙凤'.split('-'):
        word = '贾琏'
    elif word in '紫鹃-鹦哥'.split('-'):
        word = '紫鹃'
    elif word in '翠缕-缕儿'.split('-'):
        word = '翠缕'
    elif word in '香菱-甄英莲'.split('-'):
        word = '香菱'
    elif word in '豆官-豆童'.split('-'):
        word = '豆官'
    elif word in '薛蝌—邢岫烟'.split('-'):
        word = '薛蝌'
    elif word in '薛蟠—夏金桂'.split('-'):
        word = '薛蟠'
    elif word in '贾宝玉-宝玉'.split('-'):
        word = '贾宝玉'
    elif word in '林黛玉-林姑娘-黛玉'.split('-'):
        word = '林黛玉'
    if word not in names:
        continue
    counts[word] = counts.get(word, 0)+1

# 将人名按照次数排序 降序
items = list(counts.items())
# 排序规则 以次数为参考进行排序
items.sort(key=lambda x: x[1], reverse=True)
# print(items)
print('出现次数最多的是:', items[0][0], '出现了：', items[0][1], '次')
print('出现次数最少的是:', items[-1][0], '出现了：', items[-1][1], '次')
for item in items:
    print(item[0], '出现了：', item[1], '次')