#!/usr/bin/env python

import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder


def _select_feature_subset(df: pd.DataFrame) -> pd.DataFrame:
    candidate_columns = ["price", "PC1", "PC2", "PC3", "event_type", "category", "brand"]
    selected_columns = [column for column in candidate_columns if column in df.columns]

    if not selected_columns:
        raise ValueError("No suitable features were found for clustering.")

    features = df[selected_columns].copy()
    for column in features.columns:
        if not pd.api.types.is_numeric_dtype(features[column]):
            encoder = LabelEncoder()
            features[column] = encoder.fit_transform(features[column].astype(str))

    return features


def _write_cluster_counts(labels: pd.Series, output_file: str = "clusters.txt") -> None:
    counts = labels.value_counts().sort_index()
    with open(output_file, "w", encoding="utf-8") as file:
        for cluster_id, sample_count in counts.items():
            file.write(f"Cluster {cluster_id}: {sample_count} samples\n")


def run_clustering(input_csv: str) -> None:
    df = pd.read_csv(input_csv)
    features = _select_feature_subset(df)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = pd.Series(model.fit_predict(features), name="cluster")
    _write_cluster_counts(labels)
    print("Cluster counts were written to clusters.txt.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python cluster.py <input_csv>")
        sys.exit(1)

    run_clustering(sys.argv[1])


if __name__ == "__main__":
    main()
