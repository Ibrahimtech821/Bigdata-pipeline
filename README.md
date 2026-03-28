# Big Data Pipeline

A comprehensive data preprocessing, visualization, and clustering pipeline for large-scale e-commerce data analysis.

## Overview

This project implements a complete data science pipeline that:
- Cleans and preprocesses raw data
- Applies feature engineering and dimensionality reduction
- Generates visualizations and statistical summaries
- Performs clustering analysis on processed data

## Repository Structure

```
Bigdata-pipeline/
├── README.md                 # Project documentation
├── data_preprocessed.csv    # Cleaned and processed dataset (~18.6MB)
├── pre_process.ipynb        # Jupyter notebook for preprocessing exploration
├── pipeline/                # Core pipeline directory
│   ├── Dockerfile           # Docker configuration for containerization
│   ├── pre_process.py       # Data cleaning & feature transformation script
│   ├── visualize.py         # Data visualization script
│   └── cluster.py           # Clustering analysis script
└── clusters.txt             # Clustering results
```

## Branches

- **main** - Main production branch with core pipeline components
- **py-conversion** - Python conversion improvements (includes `data_raw.csv`)
- **cluster** - Clustering-specific implementations
- **Visuals** - Visualization enhancements
- **analytics-txt** - Analytics output files

## Data

### Input Data
- **Source**: Raw e-commerce transaction data
- **Download**: [Link to raw data (Google Drive)](https://drive.google.com/file/d/1MW6lzze7AWBtzM4xwrL3XCTfkAeV4eEc/view?usp=drive_link)
- **Size**: ~18.5MB (raw), ~18.6MB (preprocessed)

### Output Data
- **data_preprocessed.csv** - Cleaned and transformed dataset ready for analysis

## Pipeline Stages

### Stage 1: Data Cleaning (`pre_process.py`)
- Removes irrelevant columns: `event_time`, `product_id`, `category_id`, `user_id`, `user_session`
- Removes duplicate rows
- Drops rows with missing values
- Extracts main category from `category_code`

### Stage 2: Feature Engineering
- **Brand Encoding**: Reduces brands to top 10 + "other" category
- **Label Encoding**: Encodes categorical features:
  - `event_type` → `event_type_encoded`
  - `brand` → `brand_type_encoded`
  - `category` → `category_type_encoded`
- **Scaling**: StandardScaler applied to price column
- **Discretization**: Price binned into 5 categories:
  - Budget (0-50)
  - Mid-range (50-500)
  - Premium (500-1000)
  - High-end (1000-2000)
  - Luxury (2000+)

### Stage 3: Dimensionality Reduction
- **PCA (Principal Component Analysis)**: Reduces features to 3 principal components
- Preserves maximum variance while reducing dimensionality
- Generates `PC1`, `PC2`, `PC3` features

### Stage 4: Visualization (`visualize.py`)
Generates comprehensive 4-plot summary:
1. **Event Type Distribution** - Count plot of events
2. **Price Distribution by Category** - Box plot analysis
3. **Price Bin vs Event Type** - Relationship visualization
4. **Feature Correlation Heatmap** - Correlation matrix of encoded features

Output: `summary_plot.png`

### Stage 5: Clustering Analysis
Automated clustering pipeline produces `clusters.txt` with results

## Technologies & Dependencies

- **Python 3.11+**
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn (preprocessing, decomposition)
- **Visualization**: matplotlib, seaborn
- **Containerization**: Docker

### Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy requests
```

## Quick Start

### Local Execution
```bash
# Run preprocessing
python pipeline/pre_process.py data_raw.csv

# Generates: data_preprocessed.csv, summary_plot.png, clusters.txt
```

### Docker Execution
```bash
# Build Docker image
docker build -t bigdata-pipeline ./pipeline

# Run container
docker run -it bigdata-pipeline
python pre_process.py data_raw.csv
```

## Output Files

| File | Description |
|------|-------------|
| `data_preprocessed.csv` | Cleaned dataset with engineered features |
| `summary_plot.png` | 4-panel visualization of data distributions |
| `clusters.txt` | Clustering results and assignments |

## Project Workflow

```
Raw Data → Preprocessing �� Feature Engineering → 
Dimensionality Reduction → Visualization → Clustering → Results
```

## Key Metrics

- Original dataset: Multiple columns of transaction data
- Preprocessed dataset: Price categories + 3 principal components
- Variance Retained by PCA: Typically 80-90% with 3 components
- Category Distribution: Multiple product categories analyzed

## Notes

- The pipeline is automated and runs end-to-end via `pre_process.py`
- Each stage prints progress and data shape information
- Docker setup enables reproducible environment across systems
- Multiple branch implementations available for different use cases

## Contributers
Ibrahim Ahmed
Farida Haitham
Nardy Saleh
Ahmed Taher

## Contributing

Contributions across branches welcome. Ensure preprocessing maintains data integrity and visualization clarity.

## Data Handling

Ensure `data_raw.csv` is available in the working directory before running the pipeline. Download from the link in the Data section.

---

**Last Updated**: 2026-03-28 17:43:15 UTC  
**Python Version**: 3.11+  
**Status**: Active Development
