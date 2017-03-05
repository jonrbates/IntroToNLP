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


# import nltk
path = 'C:/nltk_data/corpora/unicode_samples/polish-lat2.txt'

import codecs
lines =  codecs.open(path, encoding='latin2').readlines()
x = lines[0]
print '\nlatin2'
print x
print repr(x)
print '\nunicode_escape'
print x.encode('unicode_escape')
print repr(x.encode('unicode_escape'))
print '\nutf8'
print x.encode('utf8')
print repr(x.encode('utf8'))
    
    
# with codecs.open(path, encoding='utf-8') as f:
#    for line in f:
#        print line


print ord('\''), '\'', repr('\'')
print ord(u'\''), u'\'', repr('\'')

a = u'\u0061'
print repr(a)
print a