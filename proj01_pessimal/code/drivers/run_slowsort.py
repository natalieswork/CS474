import time, csv, os

def slow_sort(A, i, j):
    if i >= j:
        return

    m = (i + j) // 2
    slow_sort(A, i, m)
    slow_sort(A, m + 1, j)

    if A[j] < A[m]:
        temp = A[m]
        A[m] = A[j]
        A[j] = temp

    slow_sort(A, i, j - 1)

def executeSlow (lst, iters, file_name):
    lst_len = len(lst)
    for _ in range(iters):
        lst_copy = lst.copy()
        start_time = time.time()
        slow_sort(lst_copy, 0, lst_len - 1)
        delta = time.time() - start_time

        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([lst_len, "{:.10f}".format(delta*1000)])

# Main Program Starts Here:

# Define Variables
cwd = os.getcwd()
slowsort_path = cwd+"/csvdata/slowsort.csv"
iterations = 10
data_files = ['1_data.txt', '2_data.txt', '3_data.txt', '4_data.txt',
                '5_data.txt', '6_data.txt', '7_data.txt', '8_data.txt', '9_data.txt',
                  '10_data.txt', '11_data.txt', '12_data.txt', '13_data.txt', '14_data.txt',
                   '15_data.txt', '16_data.txt', '17_data.txt', '18_data.txt', '19_data.txt',
                   '20_data.txt', '25_data.txt', '30_data.txt', '40_data.txt',
                    '50_data.txt', '75_data.txt', '100_data.txt', '125_data.txt', '150_data.txt',
                  '175_data.txt', '200_data.txt', '205_data.txt', '210_data.txt', '220_data.txt',
                   '225_data.txt', '250_data.txt', '300_data.txt', '400_data.txt', '500_data.txt']
# Create CSV data file
with open(slowsort_path, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["list_size", "slow_time"])

# Read in data file and populate Python list
for datafile in data_files:
        with open(cwd+"/rawdata/"+datafile, 'r') as file:
            data_list = file.read().splitlines()
            for i in range(len(data_list)):
                data_list[i] = int(data_list[i])
            executeSlow(data_list, iterations, slowsort_path)
                