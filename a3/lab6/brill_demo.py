#!/usr/bin/env python3

from nltk.tbl.demo import postag
postag(num_sents=None, train=0.7665)
# if we set num_sents to None, it will use the whole treebank corpus.
# We want this, so we can compare the results to the CRF and HMM we
# tested earlier. If we set train ratio to 0.7665, the train set will have
# 3000 sentences, just like in previous taggers. The other params are default.

# Accuracy: 92.42%
#
# Top Three Rules are:
#   1. NN->VB if Pos:-NONE-@[-2] & Pos:TO@[-1]
#   2. VBP->VB if Pos:MD@[-3,-2,-1]
#   3. VBP->VB if Pos:TO@[-1]
#
# (In this case)Based on accuracy, we can say that brill tagger is better than hmm
# The difference between CRF and brill is very less and CRF is slightly ahead in performance.
# So CRF is better (in this case).
