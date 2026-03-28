#!/bin/bash
mkdir -p results

docker cp bigdata:/app/pipeline/data_preprocessed.csv results/
docker cp bigdata:/app/pipeline/insight1.txt results/
docker cp bigdata:/app/pipeline/insight2.txt results/
docker cp bigdata:/app/pipeline/insight3.txt results/
docker cp bigdata:/app/pipeline/clusters.txt results/
docker cp bigdata:/app/pipeline/summary_plot.png results/

docker stop bigdata
docker rm bigdata

echo "Done! All outputs copied to results/"