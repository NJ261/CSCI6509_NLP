#!/usr/bin/env python3

from nltk.corpus import gutenberg
from nltk import FreqDist

# Count each token in austen-persuasion.txt of the Gutenberg collection
list_of_words = gutenberg.words("austen-persuasion.txt")
fd = FreqDist(list_of_words) # Frequency distribution object

print("Total number of tokens: " + str(fd.N())) # number of words: 98171
print("Number of unique tokens: " + str(fd.B())) # unique words: 6132 
print("Top 10 tokens:") # third common most token is `to`

for token, freq in fd.most_common(10):
	print(token + "\t" + str(freq))
