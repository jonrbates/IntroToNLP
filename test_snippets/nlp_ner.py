# -*- coding: utf-8 -*-
"""
Named Entity Recognition
"""

import nltk

# nltk.download()

sent = nltk.corpus.treebank.tagged_sents()[0]
print nltk.ne_chunk(sent, binary=False)

text = r'Uncle Sam was never a U.S. president. He was not even a real person.'
tokens = nltk.word_tokenize(text)
normalized_tokens = [t.lower() for t in tokens]
sent = nltk.pos_tag(normalized_tokens)
print nltk.ne_chunk(sent, binary=False)
print nltk.ne_chunk(nltk.pos_tag(tokens), binary=False)
