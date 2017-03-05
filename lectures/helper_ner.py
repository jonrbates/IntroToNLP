# -*- coding: utf-8 -*-
"""
Helper functions for exploring NER components of NLTK.

Use Case:
    text = nltk.corpus.reuters.raw(nltk.corpus.reuters.fileids()[0])
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)


For more inspiration, see 
http://blog.yhat.com/posts/named-entities-in-law-and-order-using-nlp.html
https://gist.github.com/onyxfish/322906

Created on Sun Jan 01 18:47:34 2017

@author: Jonathan
"""

import nltk

###########################################################################
###########################################################################

def extract_trees(x):
    """
    Extract all trees from a chunked sentence.
    """
    all_trees = []    
    if isinstance(x,nltk.tree.Tree):        
        all_trees.append(x)
        # print len(t), t.height()
        for child in x:
            all_trees.extend(extract_trees(child))        
    return all_trees
    
###########################################################################
###########################################################################

    
def print_sentence_trees(x):
    """
    Print all trees in a sentence.
    """
    for t in extract_trees(x):
        if t.label() not in ['S']:
            # print t.pformat()
            t.pprint()
    
###########################################################################
###########################################################################

def get_all_named_entities(chunked_sentences, structure=None):
    """
    Return all the named entities in a text, given the chunked sentences.
    """
    all_trees = []
    for sent in chunked_sentences:    
        all_trees.extend(extract_trees(sent))
    
    named_entities = []
    for t in all_trees:
        if t.label() not in ['S']:
            if structure == 'tree':
                named_entities.append(t) 
            elif structure == 'string':             
                named_entities.append(t.pformat())
            else:
                named_entities.append(t.label())
    return named_entities

###########################################################################
###########################################################################

    
def print_named_entities_per_sentence(sentences, chunked_sentences):
    """
    Print named entities one sentence at a time.
    """
    for i, x in enumerate(chunked_sentences):
        print sentences[i]
        print_sentence_trees(x)
        print '\n', '-'*80, '\n\n'