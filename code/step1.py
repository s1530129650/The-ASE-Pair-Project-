#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: Eron time:2018/10/22 0022
import time
import re
start = time.time()
from string import punctuation           #Temporarily useless
 
'''function：Calculate the word frequency of each line
    input:  line : a list contains a string for a row
            counts: an empty  dictionary 
    ouput:  counts: a dictionary , keys are words and values are frequencies
    data:2018/10/22
'''
def ProcessLine(line,counts):
    #Replace the punctuation mark with a space
    #line=ReplacePunctuations(line)
    line = re.sub('[^a-z0-9]', ' ', line)
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return  counts


'''function：Replace the punctuation mark with a space
    input:  line : A list containing a row of original strings
    ouput:  line: a list whose punctuation is all replaced with spaces
    data:2018/10/22
'''
def ReplacePunctuations(line):
    for ch in line :
        #Create our own symbol list
        tags = [',','.','?','"','“','”','—']
        if ch in tags:
            line=line.replace(ch," ")
    return line

'''function：Create a taboo "stopwords.txt"
    input:  line : A list contains all the words in the "Gone With The Wind.txt"
    ouput:  nono
    data:2018/10/23
'''
def CreatStopWordsTxt(list):
    file = open('stopwords.txt', 'w')

    for  str in list:
        file.write(str+'\t')
    file.close()

'''function：Remove any words that do not meet the requirements
    input: dict : A dict whose keys are words and values are frequencies
    ouput: dictProc : A  removed undesirable words dict
    data:2018/10/23
'''
def RemoveUndesirableWords(dict):
    wordsCount = 0  # Number of words
    wordsCount = sum(dict.values())
    dictProc = dict.copy();
    for temp in list(dict):
        if temp[0].isdigit():
            del dictProc[temp]
        else:
            dictProc[temp] = round(dictProc[temp] / wordsCount, 4)
    return dictProc



def main():
    file = open("Gone With The Wind.txt",'r')
    count = 10 #Show the top count  words that appear most frequently

    alphabetCountsOrg={}       # Creates an empty dictionary used to calculate word frequency

    for line in file:
        alphabetCountsOrg = ProcessLine(line.lower(), alphabetCountsOrg) #Calculate the word frequency of each line

    alphabetCounts = RemoveUndesirableWords(alphabetCountsOrg) #Remove any words that do not meet the requirements


    pairs = list(alphabetCounts.items())    #Get the key-value pairs from the dictionary
    items = [[x,y]for (y,x)in pairs]        #key-value pairs in the list exchange locations, data pairs sort
    items.sort(reverse=True)

    #Notice we didn't order words of the same frequency

    for i in range(count ):
        print(items[i][1] + "\t" + str(items[i][0]))
    file.close()
    #CreatStopWordsTxt(alphabetCounts.keys())

 
if __name__ == '__main__':
    main()

end = time.time()
print (end-start)