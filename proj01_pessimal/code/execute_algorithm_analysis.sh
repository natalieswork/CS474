#!/bin/bash

# Generate random integer data files
python generate_data_files.py &

# Capture the PID
pid1=$!

# Wait for files to generate
wait $pid1

# Run both driver programs in parallel time
python run_slowsort.py &
pid2=$!

python run_bozosort.py &
pid3=$!

# Wait for both parallel programs to finish
wait $pid2
wait $pid3

# Create plot from csv, wait until program is finished
python create_graph_from_csv.py &
pid4=$!
wait $pid4

# When all Python scripts complete, close script 
echo "All programs have finished."
