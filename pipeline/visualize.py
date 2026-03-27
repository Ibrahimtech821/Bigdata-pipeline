

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import sys


print("Loading data...")
df = pd.read_csv(sys.argv[1])


print("Generating plots...")

plt.figure(figsize=(20, 16))

# Plot 1 - Event Type Distribution
plt.subplot(2, 2, 1)
sns.countplot(data=df, x='event_type')
plt.title('Event Type Distribution')

# Plot 2 - Price Distribution by Category
plt.subplot(2, 2, 2)
sns.boxplot(y='price', x='category', data=df)
plt.xticks(rotation=90)
plt.title('Price Distribution by Category')


plt.subplot(2, 2, 3)
sns.countplot(data=df, x='price_bin', hue='event_type')
plt.title('Price Bin vs Event Type')

plt.subplot(2, 2, 4)
cols = ['event_type', 'brand', 'price', 'category', 'price_bin']
df_heat = df[cols].copy()
df_heat['event_type'] = df_heat['event_type'].astype('category').cat.codes
df_heat['brand'] = df_heat['brand'].astype('category').cat.codes
df_heat['category'] = df_heat['category'].astype('category').cat.codes
df_heat['price_bin'] = df_heat['price_bin'].astype('category').cat.codes
corr = df_heat.corr()
sns.heatmap(corr, annot=True, fmt=".4f", cmap="Blues", linewidths=0.5)
plt.title("Feature Correlation Heatmap")


plt.tight_layout()
plt.savefig('summary_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved summary_plot.png!")


subprocess.run(["python", "cluster.py", sys.argv[1]])