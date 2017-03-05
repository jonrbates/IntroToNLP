# -*- coding: utf-8 -*-
"""
DEF. Normalize, Stem, Lemmatize

One usually *normalizes* text to lowercase so that the distinction
between "The" and "the" is ignored.
A next possible step is to *stem* the text by stripping off any affixes.
Another possible further step is to map the resulting form (i.e. stem) 
to an entry in a dictionary; the dictionary entry is called a lemma, hence 
this step being called *lemmatization*.
"""

import nltk

############################################
# Basics
############################################

test_text = r'Was the \'cat\' with the Ph.D. lying on the mat? [yes] no!!! :) \r\n'
# test_text_u = u'Was the \'cat\' with the Ph.D. lying on the mat? [yes] no!!! :) \r\n'

# Tokenize
print "\nTokenizers\n"
print nltk.word_tokenize(test_text)
print nltk.wordpunct_tokenize(test_text)

# Stem
tokens = nltk.word_tokenize(test_text)
print "\nStemmers\n"
print [nltk.PorterStemmer().stem(t) for t in tokens]
print [nltk.LancasterStemmer().stem(t) for t in tokens]
       
       
# A stemming test
tokens = ['lie', 'lied', 'lay', 'lies', 'lying', 'FALL', 'fell', 'Falling', 'falls', 'falled']
print "\nStemmers\n"
print [nltk.PorterStemmer().stem(t) for t in tokens]
print [nltk.LancasterStemmer().stem(t) for t in tokens]
   
############################################
# Example 3.1
############################################

class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))
        
    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = width/4    # words in the context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])            
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])            
            print ldisplay, rdisplay
    
    def _stem(self, word):
        return self._stemmer.stem(word).lower()
            
   
# Test Example

text = IndexedText(nltk.PorterStemmer(),
                   nltk.corpus.reuters.words(categories='trade'))

text.concordance('lying')
text.concordance('falling')
