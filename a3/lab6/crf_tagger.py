#!/usr/bin/env python3

# Import the toolkit and tags
from nltk.corpus import treebank
# Import CRF module
from nltk.tag import crf

# Train data - pretagged
train_data = treebank.tagged_sents()[:3000]
# Train data - pretagged
test_data = treebank.tagged_sents()[3000:]

# Setup a trainer with default(None) values
# Train with the data
tagger = crf.CRFTagger()
tagger.train(train_data, 'model.crf.tagger')
print(tagger)
# Prints the basic data about the tagger

print(tagger.evaluate(test_data))
# --------------------------
# Name          | Accuracy
# --------------|-----------
# crf_tagger    | 94.76%
# hmm_tagger    | 36.84
# --------------------------
# Here, in this case we can conclude that crf_tagger is better.
