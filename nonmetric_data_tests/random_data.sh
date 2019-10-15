#!/bin/bash
# eval python generate_dataset.py/
circ_num=$((($RANDOM%10)+1))
rand_val=$((($RANDOM%2)+1))
echo $circ_num > input_vals.txt
for i in $(seq 1 $circ_num); do 
    circ_data_points=$((($RANDOM%400)+100))
    echo $circ_data_points >> input_vals.txt
    done
echo $rand_val $(($rand_val+2)) >> input_vals.txt
for i in $(seq 1 $circ_num); do 
    circ_data_points=$((($RANDOM%4)+4))
    echo $circ_data_points >> input_vals.txt
    done
