#!/bin/bash

CONTAINER=${1:-bigdata}

mkdir -p results

docker cp $CONTAINER:/app/pipeline/data_preprocessed.csv results/
docker cp $CONTAINER:/app/pipeline/insight1.txt results/
docker cp $CONTAINER:/app/pipeline/insight2.txt results/
docker cp $CONTAINER:/app/pipeline/insight3.txt results/
docker cp $CONTAINER:/app/pipeline/clusters.txt results/
docker cp $CONTAINER:/app/pipeline/summary_plot.png results/

docker stop $CONTAINER
docker rm $CONTAINER

echo "Done! All outputs copied to results/"