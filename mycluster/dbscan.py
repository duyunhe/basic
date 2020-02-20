# -*- coding: utf-8 -*-
# @Time    : 2018/7/14
# @Author  : Clark Du
# @简介    : 
# @File    : dbscan.py

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import KDTree


X, y = make_blobs(n_samples=500,
                  n_features=2,
                  centers=[[-0.5, -1], [0, 0], [1, 1], [0.5, 0]],
                  cluster_std=[0.4, 0.1, 0.3, 0.2],
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)  # For reproducibility
plt.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
            c='K', edgecolor='k')
tree = KDTree(X, leaf_size=2)
dist, ind = tree.query(X[:0], k=3)
plt.show()
