##https://pythonprogramminglanguage.com/kmeans-text-clustering/
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np



data = pd.read_csv('joinedLineItems.csv', encoding='utf-8')

print(data.head())

data = data['Description'].dropna()

print(data.head())

vectoriser = TfidfVectorizer(stop_words='english')

X = vectoriser.fit_transform(data.values.astype('U'))
true_k = 2
kmodel = KMeans(n_clusters=true_k, init='k-means++', max_iter=10000, n_init=1)
kmodel.fit(X)

print('Top terms per cluster:')
order_centroids = kmodel.cluster_centers_.argsort()[:, ::-1]
terms = vectoriser.get_feature_names()
for i in range(true_k):
    print('Cluster %d' % i),
    for ind in order_centroids[i, :10]:
        print(' %s ' % terms[ind]),
    print

y_km = kmodel.fit_predict(X)
print(y_km)
print(kmodel.cluster_centers_)


