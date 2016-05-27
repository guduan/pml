#!/bin/bash

for file in test*.py; do 
    dls-python $file
done
