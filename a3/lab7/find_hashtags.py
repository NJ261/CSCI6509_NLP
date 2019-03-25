#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:12:50 2019

@author: nirav
"""
import pandas as pd
from nltk.tokenize import TweetTokenizer
import re
    
class Lab7:
    
    # Load CSV data
    def loadData(self, fileName):
        dataset = pd.read_csv(fileName)
        return dataset
    
    # take input dataframe, column names (screen_name, text)
    # returns datalist for word tokenization and screen_name's unique values
    def arrangeData(self, dataset, headerColumnName, dataColumnName):
    
        columnHeaders = list(set(dataset[headerColumnName]))
        columnData = list(dataset[dataColumnName])
        outerList, innerList = [], []
        
        for headers in range(0, len(columnHeaders)):
            for data in range(0, len(columnData)):
                if dataset['screen_name'][data] == columnHeaders[headers]:
                    innerList.append(columnData[data])
            outerList.append(innerList)
            innerList = []
        return outerList, columnHeaders
    
    # find hashtags from given datalist and return hashtags
    def findHashTags(self, dataList): 
        hashTags, tempList = [], []
        for i in range(0, len(dataList)):
            for j in range(0, len(dataList[i])):
                tempVar = re.findall(r"#(\w+)", dataList[i][j])
                if len(tempVar) != 0:
                    tempList.append(tempVar)
            tempList = list(set(item for sublist in tempList for item in sublist))
            hashTags.append(tempList)
            tempList = []
        return hashTags
    
    # takes datalist and nltk tokenizer and returns unique tokens    
    def tokenizeData(self, tokenizer, dataList): 
        outerList, innerList = [], []  
        for listNumber in range(0, len(dataList)):
            for item in range(0, len(dataList[listNumber])):
                innerList.append(tokenizer.tokenize(dataList[listNumber][item]))
            innerList = list(set(item for sublist in innerList for item in sublist))
            outerList.append(innerList)
            innerList = []
        return outerList
    
    # takes unique tokens, hashtags and screen_name's unique values
    # print outout
    def printOutput(self, columnHeaders, uniqueWords, hashTags):
        for headers in range(0, len(columnHeaders)):
            print('{}:'.format(columnHeaders[headers]))
            print('* unique tokens: {}'.format(', '.join(uniqueWords[headers])), "\n")
            print('* unique hashtags: #{}'.format(', #'.join(hashTags[headers])), "\n\n")


class MainClass():

    def mainMethod():         
        lab7 = Lab7()
        dataset = lab7.loadData('tweets.csv')
        dataList, columnHeaders = lab7.arrangeData(dataset, 'screen_name','text')
        
        tokenizer = TweetTokenizer()
        uniqueWords = lab7.tokenizeData(tokenizer, dataList)
        hashTags = lab7.findHashTags(dataList)
        lab7.printOutput(columnHeaders, uniqueWords, hashTags)

if __name__ == "__main__":
    
    MainClass.mainMethod()