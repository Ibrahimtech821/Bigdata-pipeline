#!/bin/bash
mkdir -p results

docker cp pipeline:/app/pipeline/data_raw.csv results/
docker cp pipeline:/app/pipeline/data_preprocessed.csv results/
docker cp pipeline:/app/pipeline/insight1.txt results/
docker cp pipeline:/app/pipeline/insight2.txt results/
docker cp pipeline:/app/pipeline/insight3.txt results/
docker cp pipeline:/app/pipeline/clusters.txt results/
docker cp pipeline:/app/pipeline/summary_plot.png results/

docker stop pipeline
docker rm pipeline

echo "Done! All outputs copied to results/"