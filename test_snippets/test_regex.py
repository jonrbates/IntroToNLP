# -*- coding: utf-8 -*-

import nltk


# Get Reuters Corpus
x = nltk.Text(nltk.corpus.reuters.words(categories='trade'))
y = x.findall(r'<.*> <.*> <f[ea]ll*>')

wordlist = [w.lower() for w in x.vocab().keys()]

import re
print [w for w in wordlist if re.search('^[fF].[lL]{2,}',w)]
       