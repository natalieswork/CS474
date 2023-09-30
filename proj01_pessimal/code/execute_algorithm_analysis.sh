#!/bin/bash

# Generate random integer data files
python3 drivers/generate_data_files.py &

# Capture the PID
pid1=$!

# Wait for files to generate
wait $pid1

# Run both driver programs in parallel time
python3 drivers/run_slowsort.py &
pid2=$!

python3 drivers/run_bozosort.py &
pid3=$!

# Wait for both parallel programs to finish
wait $pid2
echo "All SlowSort Runs Completed."
wait $pid3
echo "All BozoSort and SlowSort Runs Completed."

# Create plot from csv, wait until program is finished
python3 drivers/create_graph_from_csv.py &
pid4=$!
wait $pid4

# When all Python scripts complete, close script 
echo "Runs completed, graphs generated."
