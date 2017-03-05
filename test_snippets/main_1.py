# -*- coding: utf-8 -*-
"""
NLP TESTS

Many of the definitions are taken from the NLTK book
[]

"""

import sys
print sys.version
print sys.platform

import psutil
print psutil.cpu_count()
print psutil.virtual_memory()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


import nltk
nltk.download()
# Get reuters corpus
#   corpora/stopwords
#   tokenizers/punkt/english.pickle

"""
The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. 
The documents have been classified into 90 topics, and grouped into two sets, 
called "training" and "test"; 
thus, the text with fileid 'test/14826' is a document drawn from the test set. 
"""

# Get Reuters Corpus
from nltk.corpus import reuters

# Overview of Corpus
print 'The Reuters corpus has documents with multiple categories: '
print reuters.categories()[:13]
print 'etc.'
 
print 'A total of ', len(reuters.fileids()), ' training and test documents.'

# Look at particular document in corpus;
# specifically a document with the coffee category
docid = reuters.fileids(categories='coffee')[0] # a coffee-related document
print docid

# Print the raw text of the document
raw_text = reuters.raw(docid)
print raw_text

# Print other categories the document belongs to
print 'Other categories in this document: ', reuters.categories(docid)

# This document has already been preprocessed.
# Here are some of the things we can do with it...

# Look at tokens in the document
w = reuters.words(docid)
print w[:20]

# 
x = nltk.Text(w)

from nltk import FreqDist
fdist = FreqDist(x)
print 'Number of times coffee occurs = ', fdist['coffee']
fdist.plot(30)  # Frequency plot of tokens

x.dispersion_plot(['trade','coffee','oil','rubber','exchange'])


print x.concordance('coffee')



# Now get large collection of documents
x = nltk.Text(nltk.corpus.reuters.words(categories=['trade','coffee']))
       
x.dispersion_plot(['trade','coffee','oil','rubber','exchange'])
print x.concordance('coffee')

# similarity test
print '\nTokens similar to \'fell\':\n', x.similar('fell')
print '\nTokens similar to \'economy\':\n', x.similar('economy')

print '\nCommon contexts for \'oil\' and \'coffee\':\n', x.common_contexts(['oil','coffee'])

# DEF. A *collocation* is a sequence of words that occur together 
# unusually often; e.g. "hip replacement", "emergency room"
print x.collocations(num=10,window_size=3)






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# How to process raw text
# See Chapter 3 of NLTK book

print raw_text[:300]

# Step 1. Tokenize the text
#
# DEF. A token is the technical name for a sequence of characters,
# e.g. "sugery", "hip", "ward", 
# that we want to treat as a group. 
#
# DEF. The *vocabulary* of a text is the set of tokens that it uses.
#
tokens = nltk.word_tokenize(raw_text)
print tokens[:30]

# Tokenizer 1
test_text = 'Smith Ph.D. and :) ? Checkbox: [yes] no!!! \r\n'
print nltk.word_tokenize(test_text)
# Tokenizer 2
print nltk.wordpunct_tokenize(test_text)

# Step 2. Create an NLTK text
text = nltk.Text(tokens)

# Step 3. Normalize the words
#
# TODO. To normalize is to
#
words = [w.lower() for w in text]

# Step 4. Build the vocabulary
vocab = sorted(set(words))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# string processing: tokenize, stem

tokenizer = nltk.tokenize.TreebankWordTokenizer()
stemmer = nltk.stem.porter.PorterStemmer()
xs = [stemmer.stem(word.lower()) for word in tokenizer.tokenize(r)]
print xs


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# nltk.collocations
# nltk.tag
# nltk.chunk
   
# TODO. Word sense disambiguation for homonyms.
# "Serve" has several senses: give food or drink; hold office; put ball into play
# In clinical domain, "pt" may stand for patient; prothrombin time; physical therapist



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# LDA and such
print reuters.words(categories='coffee')[:30]

cfd = nltk.ConditionalFreqDist((category, word.lower())
                                for category in ['coffee', 'corn', 'wheat']
                                for word in reuters.words(categories=category))

cfd.tabulate(samples=['barley','petroleum','brazil','nitrates','moisture','weather'])
cfd.plot(samples=['barley','petroleum','brazil','nitrates','moisture','weather'])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# TODO. The future
# 1. IBM's Watson on Jeopardy and Question Answering Systems
# 2. Spoken Dialogue Systems

# TODO. Challenges
# 1. WSD
# 2. Pronoun Resolution

