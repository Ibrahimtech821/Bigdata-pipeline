#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
import subprocess
import sys

print("Loading data...")
chunks = []
for chunk in pd.read_csv(sys.argv[1], chunksize=100000):
    chunks.append(chunk)
df = pd.concat(chunks, ignore_index=True)
print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")


print("\n Data Cleaning ")

df.drop(['event_time','product_id','category_id','user_id','user_session'], axis=1, inplace=True)
print("Dropped useless columns")

df.drop_duplicates(inplace=True)
print(f"After removing duplicates: {df.shape[0]} rows")

df.dropna(inplace=True)
print(f"After dropping nulls: {df.shape[0]} rows")

df['category'] = df['category_code'].str.split('.').str[0]
df.drop('category_code', axis=1, inplace=True)
print(f"Extracted main category: {df['category'].nunique()} unique categories")


print("\n Feature Transformation ")

top_brands = df['brand'].value_counts().nlargest(10).index
df['brand'] = df['brand'].apply(lambda x: x if x in top_brands else 'other')
print("Reduced brands to top 10 + other")

encode = LabelEncoder()
df['event_type_encoded'] = encode.fit_transform(df['event_type'])
df['brand_type_encoded'] = encode.fit_transform(df['brand'])
df['category_type_encoded'] = encode.fit_transform(df['category'])
print("Label encoded: event_type, brand, category")

scaler = StandardScaler()
df['price_scaled'] = scaler.fit_transform(df[['price']])
print("Scaled price column")


print("\n Stage 3: Dimensionality Reduction")

features = ['event_type_encoded', 'category_type_encoded', 'brand_type_encoded', 'price_scaled']
pca = PCA(n_components=3)
pcs = pca.fit_transform(df[features])
df[['PC1', 'PC2', 'PC3']] = pcs
print(f"PCA explained variance: {pca.explained_variance_ratio_}")
print(f"Total variance kept: {sum(pca.explained_variance_ratio_):.2%}")

df.drop(['event_type_encoded', 'brand_type_encoded', 'category_type_encoded', 'price_scaled'], axis=1, inplace=True)


print("\n Stage 4: Discretization")

bins = [0, 50, 500, 1000, 2000, float('inf')]
labels = ['budget', 'mid-range', 'premium', 'high-end', 'luxury']
df['price_bin'] = pd.cut(df['price'], bins=bins, labels=labels)
print(f"Price bins distribution:\n{df['price_bin'].value_counts()}")

# save output
df.to_csv('data_preprocessed.csv', index=False)
print(f"\nSaved data_preprocessed.csv — Shape: {df.shape}")


subprocess.run(["python", "analytics.py", "data_preprocessed.csv"])