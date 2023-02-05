#!/bin/bash
for file in data/*; do
    for i in 1 2 3 4 5 6 7 8; do
    echo "Workers $i file: $file";
    python2 main.py $i $file
    done
done