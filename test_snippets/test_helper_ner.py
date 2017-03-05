# -*- coding: utf-8 -*-
"""

"""

import nltk
import nlp_helper_ner as nlph

text = nltk.corpus.reuters.raw(nltk.corpus.reuters.fileids()[0])
sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

named_entities = nlph.get_all_named_entities(chunked_sentences, structure='string')
unique_named_entities = set(named_entities)
for l in unique_named_entities:
    print l
    
# ne_chunk has to be run again; 
# memory clears after reading it...
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False) 
named_entities = nlph.get_all_named_entities(chunked_sentences, structure=None)
unique_named_entities = set(named_entities)
for l in unique_named_entities:
    print l

# ne_chunk has to be run again; 
# memory clears after reading it...
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False) 
nlph.print_named_entities_per_sentence(sentences, chunked_sentences)
    