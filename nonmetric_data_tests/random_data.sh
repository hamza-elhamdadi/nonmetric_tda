#!/bin/bash
circ_num=$((($RANDOM%10)+1))
rand_val=$((($RANDOM%2)+1))
dense=$(($RANDOM%2))
echo $circ_num > data_files/input_vals.txt
for i in $(seq 1 $circ_num); do 
    circ_data_points=$((($RANDOM%400)+100))
    echo $circ_data_points >> data_files/input_vals.txt
    done
echo $rand_val $(($rand_val+2)) >> data_files/input_vals.txt
for i in $(seq 1 $circ_num); do 
    circ_data_points=$((($RANDOM%4)+4))
    echo $circ_data_points >> data_files/input_vals.txt
    done
if [ $dense -eq 0 ]
then
    echo "y" >> data_files/input_vals.txt
else
    echo "n" >> data_files/input_vals.txt
fi