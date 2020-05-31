import os
import re
import pandas as pd
from collections import Counter



receipts = pd.read_csv('texts.csv', header=None)
# print(receipts.head())
# print(type(receipts))
# print(receipts.keys())
receipts['text_processed'] = receipts[1].map(lambda x: re.sub('[,\.!?^\d+\s|\s\d+\s|\s\d+$]', ' ', x))
receipts['text_processed'] = receipts['text_processed'].map(lambda x: x.lower())

# print(receipts['text_processed'].head())

import gensim
from gensim.utils import simple_preprocess


def sent_to_words(sentences):
    for sentence in sentences:
        yield (simple_preprocess(sentence, deacc=True))


data = receipts.text_processed.values.tolist()
data_words = list(sent_to_words(data))
print(data_words[:1])

bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'gratuity', 'thank', 'you', 'server', 'table', 'total', 'subtotal','service', 'due'])


def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]


def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]


import spacy

nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


def stemming(texts):
    texts_out = []
    for sent in texts:
        texts_out.append(stemmer.stem(sent))
    return texts_out


data_words_nostops = remove_stopwords(data_words)
data_words_bigrams = make_bigrams(data_words_nostops)

data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
#data_stemmed = stemming(data_words)

#counts = Counter(data_lemmatized)

print(Counter(" ".join(receipts['text_processed']).split()).most_common(25))

#print(data_lemmatized[:1])

import gensim.corpora as corpora
id2word = corpora.Dictionary(data_lemmatized)
texts = data_lemmatized
corpus = [id2word.doc2bow(text) for text in texts]

#print(corpus[:1])
"""
lda_model = gensim.models.LdaModel(corpus=corpus,
                                   id2word=id2word,
                                   random_state=100,
                                   chunksize=100,
                                   passes=10,
                                   per_word_topics=True,
                                   num_topics=5)
"""



##from pprint import  pprint
##pprint(lda_model.print_topics())
##doc_lda = lda_model[corpus]

