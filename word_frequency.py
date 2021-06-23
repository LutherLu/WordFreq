"""代码基于Python3.9, MacOS X Big Sur, 文本默认以UTF-8编码
存储，Windows环境请重新将文本编码为系统默认的GBK格式。代码中所有
缩进均为4个英文空格"""
# 引入Python正则表达式模块
import re
# 声明一个空的词频字典
frequency = {}
# 从txt文件读取内容，并将所有大写字母转换为小写
document: str = open('Data/Foreign_csr.txt', 'r').read().lower()
# 从打开的内容中匹配所有2-15字符长度的英文单词，存储到match
match = re.findall(r'\b[a-z]{2,15}\b', document)
# 对获得的match数组进行循环
for word in match:
    count = frequency.get(word, 0)
    # 每循环一次字典的key（2-15长度的单词），就在value中加1
    frequency[word] = count + 1
# 创建一个新的txt文件存放运算结果
result = open('Result/Foreign_csr - result.txt', 'w')
# 通过循环将字典中的数据写入txt文件
for key in frequency:
    result.write(f"{frequency[key]},{key}\n")
