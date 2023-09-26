import math, time, sys, random, pandas, csv, ctypes 


def executeAlgs (seqs, iters, lst_size, max_rand, use_bozo, use_slow):

    with open("../data/bozosort_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["inputSize", "delta"])

    with open("../data/slowsort_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["inputSize", "delta"])

    lib = ctypes.CDLL('./sort_algs.so') 
    
    for i in range(seqs):

        for _ in range(iters):
            bozo_lst = []
            slow_lst = []

            for _ in range(lst_size):
                rand_num_1 = random.randint(0, max_rand)
                rand_num_2 = random.randint(0, max_rand)
                bozo_lst.append(rand_num_1)
                slow_lst.append(rand_num_2)

            bozo_c_array = (ctypes.c_int * lst_size)(*bozo_lst)
            slow_c_array = (ctypes.c_int * lst_size)(*slow_lst)

            if use_bozo == True:
                bozosort_start_time = time.time()
                lib.bozosort(bozo_c_array, lst_size)
                bozosort_time = time.time() - bozosort_start_time
                with open('../data/bozosort_data.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([lst_size, "{:.10f}".format(bozosort_time*1000)])

            if use_slow == True:
                bozosort_start_time = time.time()
                lib.bozosort(slow_c_array, lst_size)
                bozosort_time = time.time() - bozosort_start_time
                with open('../data/slowsort_data.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([lst_size, "{:.10f}".format(bozosort_time*1000)])

            if use_slow == False and  use_bozo == False:
                print("Error! no supplied algorithms to run. Please define in function parameters!")
            
        lst_size = lst_size + 1


# Main Program Starts Here:

# This function call will progress through twelve sequences of tests, starting with list size 1 up to size 12.
# On each sequence, there will be 250 iterations of test, using a randomly generated list every iteration.
# The list size is designed to increase by 1 every sequence. Sequence 1 will use lists of size 1, Sequence
# 4 will use lists of size 4, so on and so forth. The maximum value of each element in any generated array is 100.
# Lastly, the parameters use_bozo and use_slow indicate which algorithm will be tested. Both can be tested. 
executeAlgs(seqs = 12, iters = 250, lst_size = 1, max_rand = 100, use_bozo = False, use_slow = True)

