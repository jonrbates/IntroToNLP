# -*- coding: utf-8 -*-
"""
Test LDA on FDA data
"""

import os
import pickle
from time import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


DIR = r'C:\Users\Jonathan\Desktop\Projects\IntroToNLP\device_events'

fname = os.path.join(DIR,r'open_fda_device_event_data.pkl')
data = pickle.load(open(fname, "rb"))
text = [x['narrative'] for x in data]


n_features = 10000
n_topics = 10
n_top_words = 8


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


# Use tf (raw term count) features for LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_features,
                                ngram_range=(1, 1),
                                stop_words='english')
t0 = time()

#
# data_samples is a list of unicode texts
#
tf = tf_vectorizer.fit_transform(text)
print("done in %0.3fs." % (time() - t0))

print("Fitting LDA models with tf features...")
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=100,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
t0 = time()
lda.fit(tf)
print("done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

"""
import nltk

w = list()
for _,_,_,text in data:
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    w = w+tagged_sentences
"""