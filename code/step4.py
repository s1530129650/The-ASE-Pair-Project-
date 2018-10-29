#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: albert time:2018/10/23 0023

import time
import re
import string
from collections import Counter

start = time.time()
from string import punctuation  # Temporarily useless

def NumWordFrequency(fileContent,number):
    fileContent = re.sub('\n|\t',' ',fileContent)
    mPunctuation = r',|;|\?|\!|\.|\:|\“|\"|\”'
    sentenceList = re.split(mPunctuation , fileContent)#Divide the text into sentences according to the punctuation marks
    wordsCounts = {}  # Creates an empty dictionary used to calculate word frequency
    for oneSentence in sentenceList:
        wordsCounts = ProcessLine(oneSentence.lower(), wordsCounts,number)  # Calculate the specified length phrase frequency
    return wordsCounts


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

class WordFinder(object):
    '''A compound structure of dictionary and set to store word mapping'''
    def __init__(self):

        self.mainTable = {}
        for char in string.ascii_lowercase:
            self.mainTable[char] = {}
        self.specialTable = {}
        #print(self.mainTable)
        for headword, related in lemmas.items():
            # Only 3 occurrences of uppercase in lemmas.txt, which include 'I'
            # Trading precision for simplicity
            headword = headword.lower()
            try:
                related = related.lower()
            except AttributeError:
                related = None
            if related:
                for word in related.split():
                    if word[0] != headword[0]:
                        self.specialTable[headword] = set(related.split())
                        break
                    else:
                        self.mainTable[headword[0]][headword] = set(related.split())
            else:
                self.mainTable[headword[0]][headword] = None
        #print(self.specialTable)
        #print(self.mainTable)
    def find_headword(self, word):
        """Search the 'table' and return the original form of a word"""
        word = word.lower()
        alphaTable = self.mainTable[word[0]]
        if word in alphaTable:
            return word

        for headword, related in alphaTable.items():
            if related and (word in related):
                return headword

        for headword, related in self.specialTable.items():
            if word == headword:
                return word
            if word in related:
                return headword
        # This should never happen after the removal of words not in valid_words
        # in Book.__init__()
        return None

    # TODO
    def find_related(self, headword):
        pass


def VerbTableFrequency(fileContent):
    global lemmas
    global  allVerbWords
    lemmas = {}
    allVerbWords = set()
    with open('verbs.txt') as fileVerb:
        # print(fileVerb.read())
        for line in fileVerb:
            # print(line)
            line = re.sub(r'\n|\s|\,', ' ', line)
            headWord = line.split('->')[0]
            # print(headWord)
            # print(headWord)
            try:
                related = line.split('->')[1]
                # print(related)

            except IndexError:
                related = None
            lemmas[headWord] = related

    allVerbWords = set()
    for headWord, related in lemmas.items():
        allVerbWords.add(headWord)
        # print(allVerbWords)
        # print("\t")
        if related:
            allVerbWords.update(set(related.split()))
            # allVerbWords.update(related)

    tempList = re.split(r'\b([a-zA-Z-]+)\b',fileContent)
    tempList = [item for item in tempList if (item in allVerbWords)]
    finder = WordFinder()
    tempList = [finder.find_headword(item) for item in tempList]

    cnt = Counter()
    for word in tempList:
        cnt[word] += 1
    #print(type(cnt))
    return cnt

def main():
    with open("Gone With The Wind.txt") as file :
        content = file.read().lower()

    outCounts = 10  # Show the top count  words that appear most frequently
    number = 1  #Phrase length
    flag = 1


    if flag == 1:
        verbFreCount = VerbTableFrequency(content)
        #print(type(cnt))

        wordsCounts ={}
        for word in sorted(verbFreCount, key=lambda x: verbFreCount[x], reverse=True):
            wordsCounts[word] = verbFreCount[word]
        print(type(wordsCounts))
        freCountNum = sum(wordsCounts.values())

        #print (freCountNum )
        for word, fre in list(wordsCounts.items())[0:outCounts]:
            print("|\t{:15}|{:<11.2f}|".format(word,fre / freCountNum))
        print("--------------------------------")


    else:
        wordsCounts = NumWordFrequency(content,number)
        wordsCounts = RemoveUndesirableWords(wordsCounts)  # Remove any words that do not meet the requirements
        wordsCounts = StopWordProcessing(wordsCounts)  # Remove the words from the "stopwords.txt"

        pairsList = list(wordsCounts.items())  # Get the key-value pairsList from the dictionary
        items = [[x, y] for (y, x) in pairsList]  # key-value pairsList in the list exchange locations, data pairsList sort
        items.sort(reverse=True)
        # Notice we didn't order words of the same frequency
        for i in range(outCounts):
            print(items[i][1] + "\t" + str(items[i][0]))


if __name__ == '__main__':
    main()

end = time.time()
print(end - start)