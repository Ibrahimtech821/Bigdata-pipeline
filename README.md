# E-commerece Pipeline

A comprehensive big data pipeline for e-commerce data preprocessing, analytics, visualization, and clustering.

## Team Members
- Ibrahim Ahmed
- Farida Haitham
- Nardy Saleh
- Ahmed Taher

---

## Repository Structure

```
customer-analytics/
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
└── results/
```

---

## Dataset

- **Source**: [eCommerce Behavior Data - Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- **File**: `2019-Oct.csv`
- **Size**: ~1.3GB
- **Rows**: ~10 million transactions
- **Columns**: event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session

---

## Pipeline Execution Flow

```
python ingest.py 2019-Oct.csv
        ↓
ingest.py
→ reads raw CSV
→ saves data_raw.csv
→ calls preprocess.py
        ↓
preprocess.py
→ Stage 1: Data Cleaning
→ Stage 2: Feature Transformation
→ Stage 3: Dimensionality Reduction (PCA)
→ Stage 4: Discretization
→ saves data_preprocessed.csv
→ calls analytics.py
        ↓
analytics.py
→ generates insight1.txt
→ generates insight2.txt
→ generates insight3.txt
→ calls visualize.py
        ↓
visualize.py
→ generates summary_plot.png (4 plots)
→ calls cluster.py
        ↓
cluster.py
→ K-Means clustering on PC1, PC2, PC3
→ saves clusters.txt
```

---

## Pipeline Stages

### Stage 1 — Data Cleaning
- Drop irrelevant columns: `event_time`, `product_id`, `category_id`, `user_id`, `user_session`
- Remove duplicate rows
- Drop rows with missing values
- Extract main category from `category_code` (e.g. `electronics.smartphone` → `electronics`)

### Stage 2 — Feature Transformation
- Reduce brands to top 10 + "other"
- Label encode: `event_type`, `brand`, `category`
- StandardScaler on `price` column

### Stage 3 — Dimensionality Reduction
- Apply PCA → reduce to 3 components (PC1, PC2, PC3)
- Total variance retained: ~97%

### Stage 4 — Discretization
- Bin price into 5 categories:
  - Budget: $0–50
  - Mid-range: $50–500
  - Premium: $500–1000
  - High-end: $1000–2000
  - Luxury: $2000+

---

## Docker Commands

### Build image
```bash
docker build -t pipeline .
```

### Run container
```bash
docker run -it --name bigdata pipeline
```

### Run pipeline inside container
```bash
python ingest.py 2019-Oct.csv
```

### Copy outputs to host and stop container
```bash
bash summary.sh
```

### Pull from Docker Hub
```bash
docker pull ibrahimtech/bigdata-pipeline:latest
```


---

## Output Files

| File | Description |
|------|-------------|
| `data_preprocessed.csv` | Cleaned and transformed dataset |
| `insight1.txt` | Average spend and top segment stats |
| `insight2.txt` | Correlation between price and PCA components |
| `insight3.txt` | Price outlier and distribution analysis |
| `summary_plot.png` | 4-panel visualization |
| `clusters.txt` | K-Means cluster counts |

---

## Sample Outputs

### insight1.txt
```
INSIGHT 1: Average Spend and Top Segment Stats
Overall - mean: $305.42, median: $157.77, std: $382.37, min: $0.88, max: $2574.07

Average Spend by Category
sport: mean $403.97, median $239.13, count 881
electronics: mean $385.20, median $223.68, count 21757
computers: mean $365.67, median $178.64, count 11376
country_yard: mean $332.37, median $234.97, count 207
appliances: mean $278.55, median $164.71, count 18576
construction: mean $268.39, median $145.81, count 5737
furniture: mean $187.96, median $109.78, count 2608
auto: mean $168.35, median $129.94, count 1668
kids: mean $137.42, median $72.05, count 3329
medicine: mean $87.55, median $59.15, count 43
apparel: mean $75.58, median $65.64, count 1501
accessories: mean $62.54, median $39.87, count 1175
stationery: mean $55.02, median $19.05, count 270
```

### clusters.txt
```
Cluster 0: 35855 samples
Cluster 1: 24618 samples
Cluster 2: 8655 samples
```

### Price Bins Distribution
```
budget: 13753 (19.9%)
high-end: 4217 (6.1%)
luxury: 534 (0.8%)
mid-range: 42504 (61.5%)
premium: 8120 (11.7%)
```

---

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
requests
```


## Docker Hub

Image available at:
```
docker pull ibrahimtech/bigdata-pipeline:latest
```
