import math, time, sys, random

# Global Variables
RANDOM_RANGE = 10 # The integer range that will populate the list e.g 0-10
TEST_LIST_SIZE = 10 # The size of the list
SEQUENCES = 3 # The number of times the algorithms will run

# Ask user for mode, either PRODUCTION or TEST
print("MODES: PRODUCTION or TEST")
MODE = input("ENTER MODE: ")

if MODE == "PRODUCTION":
    print("UNDER CONSTRUCTION...")
    # TODO: add production code
elif MODE == "TEST":
    try:
        for i in range(SEQUENCES):
            TEST_LIST = []
            for _ in range(TEST_LIST_SIZE):
                RANDOM_NUM = random.randint(0, RANDOM_RANGE)
                TEST_LIST.append(RANDOM_NUM)
            START_SYS_TIME = time.time()
            START_CPU_TIME = time.process_time()

            # TODO: add some algorithms here with TEST_LIST...

            ELAPSED_SYS_TIME = time.time() - START_SYS_TIME
            ELAPSED_CPU_TIME = time.process_time() - START_CPU_TIME

            # TODO: add pandas for data organization
            print("System time: ",ELAPSED_SYS_TIME,"ms")
            print("CPU time: ",ELAPSED_CPU_TIME,"ms")

        # TODO: add in visual graphics and data
    except SomeException as e:
        print(f"An error occurred: {e}")
else:
    print("Type in the mode in all caps!")
    exit

