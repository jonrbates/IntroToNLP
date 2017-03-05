# -*- coding: utf-8 -*-
"""
See Section 7.6
"""
import nltk

text = nltk.corpus.reuters.raw(nltk.corpus.reuters.fileids()[7175])

# text = nltk.corpus.reuters.raw(
# nltk.corpus.reuters.fileids()[3781]) 
# <- for pattern = re.compile(r'.*')

sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
# nltk.chunk.named_entity.NEChunkParser ???

    
# INSPECT chunked_sentences[k]
for sent in chunked_sentences:
    sent.draw()
    sent.pprint()
    break


def print_semantic_relationships(extracted_rels):
    for item in extracted_rels:
        print item['subjtext'], item['untagged_filler'], item['objtext']

import re

# \b : word boundary (see p110)
# . : wildcard matches any character (p101)
# * : zero or more of previous item
# re.compile(r'.{,12} \bin\b')
# pattern = re.compile(r'.*')
pattern = re.compile(r'.{,12} \bin\b')

import nlp_helper_ner as nlph

chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
for i, sent in enumerate(chunked_sentences):
    semrels = nltk.sem.extract_rels(
                                    'ORGANIZATION', 'GPE', 
                                    sent, 
                                    pattern = pattern
                                    )    
    if len(semrels) > 0:
        print sentences[i]
        print_semantic_relationships(semrels)
        nlph.print_sentence_trees(sent)        
        print '\n', '-'*80, '\n\n'
   

       
# get interesting document
l = [6921,
7175,
7654,
8154,
8196,
8305,
8804,
8811,
8910,
9033,
9124]

pattern = re.compile(r'.{,12} \bin\b')
for k in l:
    text = nltk.corpus.reuters.raw(nltk.corpus.reuters.fileids()[k])
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)    
    for i, sent in enumerate(chunked_sentences):
        semrels = nltk.sem.extract_rels(
                                        'ORGANIZATION', 'GPE', 
                                        sent, 
                                        pattern = pattern
                                        )    
        if len(semrels) > 0:
            print k
            print_semantic_relationships(semrels)