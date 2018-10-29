#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: albert time:2018/10/22 0022
import time
import re
import operator
from string import punctuation           #所有标点

start = time.clock()

# 对文本的每一行计算字母频率的函数
def ProcessLine(line, counts):
    # 用去掉除了字母以外的其他数字
    #line=ReplacePunctuations(line)
    line = re.sub('[^a-z]','',line)
    for ch in line:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def ReplacePunctuations(line):
    tags = [',', '.', '?', '"', '“', '”', '—']
    tags = punctuation +tags
    for ch in tags :
        #这里直接用了string的标点符号库。将标点符号替换成空格
        if ch in punctuation:
            line=line.replace(ch,"")
    return line


def main():
    infile = open("Gone With The Wind.txt", 'r')
    wordsCount = 0
    # 建立用于计算26个字母的空字典
    alphabetCounts = {}
    for line in infile:
        alphabetCounts = ProcessLine(line.lower(), alphabetCounts)  # 这里line.lower()的作用是将大写替换成小写，方便统计词频
    wordsCount = sum(alphabetCounts.values())
    for temp in alphabetCounts:
        alphabetCounts[temp] = round(alphabetCounts[temp] / wordsCount,4)
    sorted(alphabetCounts.items(), key=operator.itemgetter(1))
    for v, k in alphabetCounts.items():
        print('{v}:{k}'.format(v=v, k=k))
    infile.close()


# if __name__ == '__main__':
main()

end = time.clock()
print (end-start)
