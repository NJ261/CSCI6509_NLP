#!/usr/bin/env python3

from nltk import FreqDist
# import treebank
from nltk.corpus import treebank
# import ne chunker
from nltk import chunk, tag

tempList = ["DATE", "TIME", "GPE","FACILITY","LOCATION", "MONEY","PERSON", "ORGANIZATION","PERCENT"]

data = treebank.tagged_words() # load treebank data
chunkd_data = chunk.ne_chunk(data) # chunk the data
chunkd_trees = chunkd_data.subtrees(filter=lambda t: t.label() in tempList) # select subtrees which are NE

word_fd = FreqDist([' '.join(word for word, pos in tree.leaves()) for tree in chunkd_trees])
print ("Three most common named entities are: ")

print (', '.join(word for word,freq in word_fd.most_common(3)))
# Three most common named entities are:
# U.S., New York, Japanese
