import sys, os
import pandas as pd
import numpy as np
import subprocess

df = pd.read_csv(sys.argv[1])

# INSIGHT 1: Average Spend and Top Segment Stats

cat_stats   = df.groupby('category')['price'].agg(mean='mean', median='median', count='count').sort_values('mean', ascending=False)
brand_stats = df.groupby('brand')['price'].agg(mean='mean', count='count').sort_values('mean', ascending=False)

lines = [
    'INSIGHT 1: Average Spend and Top Segment Stats',
    '',
    f"Overall - mean: ${df['price'].mean():.2f}, median: ${df['price'].median():.2f}, std: ${df['price'].std():.2f}, min: ${df['price'].min():.2f}, max: ${df['price'].max():.2f}",
    '',
    'Average Spend by Category',
]
for cat, r in cat_stats.iterrows():
    lines.append(f"{cat}: mean ${r['mean']:.2f}, median ${r['median']:.2f}, count {int(r['count'])}")

bin_counts = df['price_bin'].value_counts().sort_index()
lines += ['', 'Price Tier Distribution']
for tier, cnt in bin_counts.items():
    lines.append(f"{tier}: {cnt} ({cnt/len(df)*100:.1f}%)")

lines += ['', 'Average Spend by Brand']
for brand, r in brand_stats.iterrows():
    lines.append(f"{brand}: mean ${r['mean']:.2f}, count {int(r['count'])}")

txt = '\n'.join(lines)
print(txt)
open('insight1.txt', 'w').write(txt)
print('\nSaved insight1.txt')

# INSIGHT 2: Correlation - Price vs PCA Components

pc_cols = [c for c in ['PC1', 'PC2', 'PC3'] if c in df.columns]
price_vals = df['price'].to_numpy()

corr_results = []
for pc in pc_cols:
    r = np.corrcoef(price_vals, df[pc].to_numpy())[0, 1]
    strength  = 'strong' if abs(r) > 0.6 else 'moderate' if abs(r) > 0.3 else 'weak'
    direction = 'positive' if r > 0 else 'negative'
    corr_results.append((pc, round(r, 4), strength, direction))
corr_results.sort(key=lambda x: abs(x[1]), reverse=True)

lines = ['INSIGHT 2: Correlation - Price vs PCA Components', '']
for pc, r, strength, direction in corr_results:
    lines.append(f"price vs {pc}: r = {r:+.4f} ({strength} {direction})")
lines += ['', f"Strongest: price vs {corr_results[0][0]} (r = {corr_results[0][1]:+.4f})"]

txt = '\n'.join(lines)
print(txt)
open('insight2.txt', 'w').write(txt)
print('\nSaved insight2.txt')

# INSIGHT 3: Price Outlier and Distribution Analysis

s = df['price'].dropna()
Q1, Q3 = s.quantile(0.25), s.quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = s[(s < lower) | (s > upper)]
skew = s.skew()
dist = 'heavily right-skewed' if skew>1 else 'moderately right-skewed' if skew>0.5 else 'heavily left-skewed' if skew<-1 else 'moderately left-skewed' if skew<-0.5 else 'approximately symmetric'
outlier_by_cat   = df[df['price'].isin(outliers)].groupby('category')['price'].count().sort_values(ascending=False)
outlier_by_brand = df[df['price'].isin(outliers)].groupby('brand')['price'].count().sort_values(ascending=False)

lines = [
    'INSIGHT 3: Price Outlier and Distribution Analysis',
    '',
    f"IQR fence: [{lower:.2f}, {upper:.2f}]",
    f"Outliers: {len(outliers)} ({len(outliers)/len(s)*100:.2f}% of records)",
    f"Outlier price range: ${outliers.min():.2f} to ${outliers.max():.2f}",
    f"Skewness: {skew:.4f} - distribution is {dist}",
    '',
    'Outliers by Category',
]
for cat, cnt in outlier_by_cat.items():
    lines.append(f"  {cat}: {cnt}")
lines += ['', 'Outliers by Brand']
for brand, cnt in outlier_by_brand.items():
    lines.append(f"  {brand}: {cnt}")

txt = '\n'.join(lines)
print(txt)
open('insight3.txt', 'w').write(txt)
print('\nSaved insight3.txt')

# Chain to visualize.py
subprocess.run([sys.executable, 'visualize.py', 'data_preprocessed.csv'])