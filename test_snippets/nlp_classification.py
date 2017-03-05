# -*- coding: utf-8 -*-
"""
Train and test classification of documents in the Reuters corpus.

(cf NLTK Book Chapter 6)


"""

# Get Reuters Corpus
from nltk.corpus import reuters

# Overview of Corpus
print 'The Reuters corpus has documents with multiple categories: '
print reuters.categories()[:13]
print 'etc.'
 
print 'A total of ', len(reuters.fileids()), ' training and test documents.'

x = nltk.Text(nltk.corpus.reuters.words(categories=['trade','coffee']))
