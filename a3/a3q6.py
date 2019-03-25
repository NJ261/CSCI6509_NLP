#!/usr/bin/env python3
# Course: CSCI 6509
# Author: Nirav Jadeja
# Description: Solution a3q6.py
# Python Version: 3.7

import sys
from nltk.util import ngrams


class DataProcessing:

    def __init__(self, ngramSize, profileLength, inputFileName, outputFileName):
        self.ngramSize = ngramSize
        self.profileLength = profileLength
        self.inputFileName = inputFileName
        self.outputFileName = outputFileName

    def preprocessData(self):
        with open(self.inputFileName) as file:
            fileLine=" ".join(line.strip() for line in file)

        fileLineLength = len(fileLine) + 1
        tempFileLine = (fileLine.rjust(fileLineLength)).ljust(fileLineLength + 1)
        data = tempFileLine.replace(r" ", "_")
        return list(ngrams(data, self.ngramSize))

    def fileWrite(self, inputDict):
        count = 0
        tempDict = {}
        file=open(self.outputFileName + ".ngrams", "w+")
        for key,value in sorted(inputDict.items(), key=lambda x:(-x[1],x[0])):
            if count < self.profileLength:
                tempDict[key] = value
                file.write("%s %.16f\n" %(key, value))
                count += 1
        file.close()
        return tempDict

    def findTotalCounts(self, grams):
        tempString, tempList, frequencyCounter = "", [], {}
        for i in range(0, len(grams)):
            for j in range(0, len(grams[i])):
                tempString = tempString + grams[i][j]
            tempList.append(tempString)
            tempString = ""

        totalSum = len(tempList)
        for i in tempList:
            frequencyCounter[i] = tempList.count(i)
        return frequencyCounter, totalSum

    def findKeyValues(self, frequencyCounter, totalSum):
        floatValueList = []
        for key, value in frequencyCounter.items():
            frequencyCounter[key] = (value / totalSum)
            floatValueList.append(frequencyCounter[key])
        return floatValueList


class IDataProcessing():

    def mainMethod(ngramSize, profileLength, inputFileName, outputFileName):
        dataProcessing = DataProcessing(ngramSize, profileLength, inputFileName, outputFileName)
        grams = dataProcessing.preprocessData()
        frequencyCounter, totalSum = dataProcessing.findTotalCounts(grams)
        floatValueList = dataProcessing.findKeyValues(frequencyCounter, totalSum)
        dictValues = dataProcessing.fileWrite(frequencyCounter)
        return dictValues


class DataOperations:

    def __init__(self, dictA, dictB):
        self.dictA = dictA
        self.dictB = dictB

    def unionOfLists(self):
        result = list(set(self.dictA) | set(self.dictB))
        return result

    def compareValues(self, sortedValues):
        tempList = []
        for value in range(0, len(sortedValues)):
            if sortedValues[value] in self.dictA:
                if sortedValues[value] in self.dictB:
                    tempList.append([self.dictA[sortedValues[value]], self.dictB[sortedValues[value]]])
                else:
                    tempList.append([self.dictA[sortedValues[value]], 0])
            else:
                tempList.append([self.dictB[sortedValues[value]], 0])
        return tempList

    def calculateValues(self, comparedValues):
        tempList = []
        for i in range (0, len(comparedValues)):
            x = (2*((comparedValues[i][0] - comparedValues[i][1]) / (comparedValues[i][0] + comparedValues[i][1]))) ** 2
            tempList.append(x)
        return tempList


class IDataOperations:

    def mainMethod(dictA, dictB):
        dataOperaions = DataOperations(dictA, dictB)
        sortedValues = sorted(dataOperaions.unionOfLists())
        comparedValues = dataOperaions.compareValues(sortedValues)
        calculatedValues = dataOperaions.calculateValues(comparedValues)
        return calculatedValues


class MainClass:

    def exceptionMthod():
        try:
            arguments = sys.argv[1:]
            ngramSize = int(arguments[0])
            profileLength = int(arguments[1])
            inputFileA = str(arguments[2])
            inputFileB = str(arguments[3])

            MainClass.subMethod(ngramSize, profileLength, inputFileA, inputFileB)

        except Exception as error:
            ngramSize = int(input("enter ngram size: "))
            profileLength = int(input("enter profile length: "))
            inputFileA = str(input("Enter file A (e.g: a.txt): "))
            inputFileB = str(input("Enter file B (e.g: b.txt): "))

            MainClass.subMethod(ngramSize, profileLength, inputFileA, inputFileB)

    def subMethod(ngramSize, profileLength, inputFileA, inputFileB):
        dictA = IDataProcessing.mainMethod(ngramSize, profileLength, inputFileA, "a3q6-test1a")
        dictB = IDataProcessing.mainMethod(ngramSize, profileLength, inputFileB, "a3q6-test1b")
        calculatedValues = IDataOperations.mainMethod(dictA, dictB)
        print("CNG for %s %s a3q6-test1a a3q6-test1b: %.13f" %( ngramSize, profileLength, sum(calculatedValues)))

if __name__ == "__main__":

    MainClass.exceptionMthod()
