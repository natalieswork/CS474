import time, random, csv, os

# Bozosort Pessimal Sorting Algorithm
# Best Case:
# Average Case:
# Worst Case:
def bozosort(lst):
    while not sorted(lst) == lst:
        a, b = random.randint(0, len(lst) - 1), random.randint(0, len(lst) - 1)
        lst[a], lst[b] = lst[b], lst[a]

# Bozosort wrapper function.
# Lst is the Python list to be sorted
# iters is the number of times bozosort will be called
# file_name is the .CSV files where data will be written
def executeBozo (lst, iters, file_name):
    lst_len = len(lst)
    for _ in range(iters):
        lst_copy = lst.copy()
        start_time = time.time()
        bozosort(lst_copy)
        delta = time.time() - start_time

        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([lst_len, "{:.10f}".format(delta*1000)])


# Main Program Starts Here:

# Define Variables
cwd = os.getcwd()
bozosort_path = cwd+"/csvdata/bozosort.csv"
iterations = 10
data_files = ['1_data.txt', '2_data.txt', '3_data.txt', '4_data.txt',
                '5_data.txt', '6_data.txt', '7_data.txt', '8_data.txt', '9_data.txt',
                  '10_data.txt', '11_data.txt', '12_data.txt', '13_data.txt', '14_data.txt',
                   '15_data.txt']
# Create CSV data file

with open(bozosort_path, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["list_size", "bozo_time"])

# Read in data file and populate Python list
for datafile in data_files:
        with open(cwd+"/rawdata/"+datafile, 'r') as file:
            lines = file.read().splitlines()
            # Convert all list elements from String type to int type
            for i in range(len(lines)):
                lines[i] = int(lines[i])    
            executeBozo(lines, iterations, bozosort_path)
