#!/usr/bin/env python3
# Course: CSCI 6509
# Author: Nirav Jadeja
# Description: Solution a2q5.py
# Python Version: 3.7

import nltk, sys

# This class takes input text as a parameter and returns tokenized words
class TextOperations:
    
    def __init__(self, inputText):
        self.inputText = inputText
        
    def wordTokenize(self):
        outputText = nltk.word_tokenize(self.inputText)
        
        for word in range(0, len(outputText)):
            if word == len(outputText) - 1 :
                print(outputText[word], end='', flush=True)
            else:
                print(outputText[word], end=' ', flush=True)
            
# This class is for exceptions handling: handle user input text and input file  
class MainClass:
    
    def exceptionMthod():
        try:
            with open(sys.argv[1], 'r') as input_file:
                inputFile = input_file.read()
            textOperations = TextOperations(inputFile)
            textOperations.wordTokenize()
            
        except Exception as error:
            while True:
                try:
                    line = input()
                    if line:
                        lines.append(line)
                except EOFError:
                    break
                
            inputText = '\n'.join(lines)
            textOperations = TextOperations(inputText)
            textOperations.wordTokenize()
            
if __name__ == "__main__":
    
    MainClass.exceptionMthod()

# References:
# 1. https://www.nltk.org/_modules/nltk/tokenize.html
# 2. https://stackoverflow.com/questions/8280250/how-to-open-files-given-as-command-line-arguments-in-python
