import math, time, sys, random, pandas, csv, ctypes 
from matplotlib import pyplot as plt
import sorting_algs

# Global Variables
RANDOM_RANGE = 10 # The integer range that will populate the list e.g 0-10
TEST_LIST_SIZE = 1# The size of the list
SEQUENCES = 20 # The number of times the algorithms will run
ITERATIONS = 10

sys.setrecursionlimit(1000)

# Load C library
lib = ctypes.CDLL('./sort_algs.so') 


# Ask user for mode, either PRODUCTION or TEST
print("MODES: PRODUCTION or TEST")
MODE = input("ENTER MODE: ")



if MODE == "PRODUCTION":
    print("UNDER CONSTRUCTION...")

    # TODO: add production code

elif MODE == "TEST":
    try:
        csv_file = "test_data.csv"
        with open(csv_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["inputSize", "delta"])

        for i in range(SEQUENCES):
            xSORT_DF = pandas.DataFrame(columns=['List_Size', 'Iteration',
                                                 'Elapsed_System_Time', 'Elapsed_CPU_Time'])
            BOZOSORT_DF = pandas.DataFrame(columns=['List_Size', 'Iteration',
                                                    'Elapsed_System_Time', 'Elapsed_CPU_Time'])

            TEST_LIST = []

            for _ in range(TEST_LIST_SIZE):
                RANDOM_NUM = random.randint(0, RANDOM_RANGE)
                TEST_LIST.append(RANDOM_NUM)

            for _ in range(ITERATIONS):

                xSORT_START_SYS_TIME = time.time()
                xSORT_START_CPU_TIME = time.process_time()

            # TODO: add some algorithms here with TEST_LIST...

                # Convert Python list to C array
                c_array = (ctypes.c_int * TEST_LIST_SIZE)(*TEST_LIST)

                # Call the C quicksort function
                lib.quickSortArray(c_array, TEST_LIST_SIZE)

            # Sleep sort with TEST_LIST
            

                xSORT_ELAPSED_SYS_TIME = time.time() - xSORT_START_SYS_TIME
                xSORT_ELAPSED_CPU_TIME = time.process_time() - xSORT_START_CPU_TIME
            
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([TEST_LIST_SIZE, "{:.10f}".format(xSORT_ELAPSED_SYS_TIME*1000)])
            TEST_LIST_SIZE = TEST_LIST_SIZE * 2
    except SomeException as e:
        print(f"An error occurred: {e}")
else:
    print("Type in the mode in all caps!")
    exit

