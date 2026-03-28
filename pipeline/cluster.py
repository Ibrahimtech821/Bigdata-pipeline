#!/usr/bin/env python

import sys
import pandas as pd
from sklearn.cluster import KMeans
import subprocess
df = pd.read_csv(sys.argv[1])


features = df[['PC1', 'PC2', 'PC3']]

model = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = model.fit_predict(features)

# save to clusters.txt
counts = df['cluster'].value_counts().sort_index()
with open('clusters.txt', 'w') as f:
    for cluster_id, count in counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("Cluster counts written to clusters.txt!")