# -*- coding: utf-8 -*-
"""
Check Part-of-Speech Tagger

Nature Reviews Article, Box 1
1. Boundary Detection
2. Tokenization
3. Normalization
4. Part-of-speech tagging
5. Shallow Parsing
6. Entity Recognition

See NLTK book, Chapter 7
"""

import nltk

############################################
# Basics
############################################

test_text = r'Was the \'cat\' with the Ph.D. lying on the mat? [yes] no!!! :) \r\n'
tokens = nltk.word_tokenize(test_text)

# This tagger assigns the same tag to each token:
default_tagger = nltk.DefaultTagger('NN')
default_tagger.tag(tokens)

# What do the tags mean?


print nltk.help.upenn_tagset('NN')

# Try different taggers
print nltk.pos_tag(tokens)


#nltk.tag.brill.TaggerI.tag(tokens)