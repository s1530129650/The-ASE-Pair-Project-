#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: albert time:2018/10/23 0023

import time
import re

start = time.time()
from string import punctuation  # Temporarily useless

'''function：Calculate the word frequency of each line
    input:  line : a list contains a string for a row
            countsDict: an empty  dictionary 
    ouput:  counts: a dictionary , keys are words and values are frequencies
    data:2018/10/22
'''

def ProcessLine(sentence, countsDict,number):
    # Replace the punctuation mark with a space
    # line=ReplacePunctuations(line)
    sentence = re.sub('[^a-z0-9]', ' ', sentence)
    words = sentence.split()
    if len(words) >= number:
        for i in range(len(words)-number+1):
            countsDict[" ".join(words[i:i+number])] = countsDict.get(" ".join(words[i:i+number]), 0) + 1
    else:
        if sentence.strip()=='':   #Judge if the sentence is empty
            return countsDict
        countsDict[sentence] = countsDict.get(sentence, 0) + 1
    return countsDict


'''function：Replace the punctuation mark with a space
    input:  line : A list containing a row of original strings
    ouput:  line: a list whose punctuation is all replaced with spaces
    data:2018/10/22
'''

def ReplacePunctuations(line):
    for ch in line:
        # Create our own symbol list
        tags = [',', '.', '?', '"', '“', '”', '—']
        if ch in tags:
            line = line.replace(ch, " ")
    return line


'''function：Create a taboo "stopwords.txt"
    input:  line : A list contains all the words in the "Gone With The Wind.txt"
    ouput:  nono
    data:2018/10/23
'''

def CreatStopWordsTxt(list):
    file = open('stopwords.txt', 'w')

    for str in list:
        file.write(str + '\t')
    file.close()

'''function：Remove any words that do not meet the requirements
    input: dict : A dict whose keys are words and values are frequencies
    ouput: dict : A  removed undesirable words dict
    data:2018/10/23
'''
def RemoveUndesirableWords(dict):
    '''
        wordsCount = 0  # Number of words
        wordsCount = sum(dict.values())
    '''
    listKey = list(dict)
    for temp in listKey:
        if temp[0].isdigit():
            del dict[temp]
        #else:
           # dict[temp] = round(dict[temp] , 4)
    return dict

'''function：Remove the words from the "stopwords.txt"
    input: dict : A list transformed by a dict whose keys are words and values are frequencies
    ouput: dictProc : A list after removing stopwords
    data:2018/10/23
'''

def StopWordProcessing(dict):
    fileTabu = open("stopwords1.txt", 'r')
    stopWordlist = fileTabu.read()
    fileTabu.close()

    stopWordlist = re.sub('[^a-z0-9]', ' ', stopWordlist).split(' ')
    dictProc = dict.copy()
    for temp in dict.keys():
        if temp.strip() in stopWordlist:
            del dictProc[temp]
    return dictProc

def main():
    fileTxt = open("Gone With The Wind.txt", 'r')
    file = fileTxt.read()
    fileTxt.close()

    #Divide the text into sentences according to the punctuation marks
    file = re.sub('\n|\t',' ',file)
    mPunctuation = r',|;|\?|\!|\.|\:|\“|\"|\”'
    sentenceList = re.split(mPunctuation , file)

    count = 10  # Show the top count  words that appear most frequently
    number = 2  #Phrase length
    wordsCounts = {}  # Creates an empty dictionary used to calculate word frequency

    for oneSentence in sentenceList:
        wordsCounts = ProcessLine(oneSentence.lower(), wordsCounts,number)  # Calculate the specified length phrase frequency

    #wordsCounts = RemoveUndesirableWords(wordsCounts)  # Remove any words that do not meet the requirements
    #wordsCounts = StopWordProcessing(wordsCounts)  # Remove the words from the "stopwords.txt"

    pairsList = list(wordsCounts.items())  # Get the key-value pairsList from the dictionary

    items = [[x, y] for (y, x) in pairsList]  # key-value pairsList in the list exchange locations, data pairsList sort
    items.sort(reverse=True)

    # Notice we didn't order words of the same frequency

    for i in range(count):
        print(items[i][1] + "\t" + str(items[i][0]))

if __name__ == '__main__':
    main()

end = time.time()
print(end - start)