"""代码基于Python3.9, MacOS X Big Sur, 文本默认以UTF-8编码
存储，Windows环境请重新将文本编码为系统默认的GBK格式。代码中所有
缩进均为4个英文空格"""
# 引入Python正则表达式模块、spaCy停用词模块
import re

from spacy.lang.en.stop_words import STOP_WORDS

# 空字典
filtered_match = []
match = []
frequency = {}
all_docs = []
filtered = []

def base_doc():
    from pathlib import Path
    all_txt_files = []
    for file in Path("Foreign_CSR_txt").rglob("*.txt"):
        all_txt_files.append(file.parent / file.name)
    n_files = len(all_txt_files)
    print(n_files)
    all_txt_files.sort()
    all_txt_files[0]
    for txt_file in all_txt_files:
        with open(txt_file) as f:
            txt_file_as_string = f.read()
        all_docs.append(txt_file_as_string)
    print(all_docs)

def extract(file_name):
    # 声明一个空的词频字典
    frequency = {}
    # 从txt文件读取内容，并将所有大写字母转换为小写
    document: str = open(f'Data/{file_name}.txt', 'r').read().lower()
    # 从打开的内容中匹配所有2-15字符长度的英文单词，存储到match
    match = re.findall(r'\b[a-z]{2,15}\b', document)
    # 在match数组中去处停用词，并创建过清洗后的数组
    for item in match:
        if item not in STOP_WORDS:
            filtered_match.append(item)
        else:
            continue

def freq():
    # 对获得的match数组进行循环
    for word in filtered_match:
        count = frequency.get(word, 0)
        # 每循环一次字典的key（2-15长度的单词），就在value中加1
        frequency[word] = count + 1
    # 创建一个新的txt文件存放运算结果
    result = open(f'Result/{fn} - result - 2021.txt', 'w')
    # 通过循环将字典中的数据写入txt文件
    for key in frequency:
        result.write(f"{frequency[key]},{key}\n")

fn = input("File name in Data folder:")
extract(fn)
freq()
