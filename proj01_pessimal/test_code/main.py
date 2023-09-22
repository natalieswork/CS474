import math, time, sys, random, pandas, csv, ctypes 


def executeAlgs (seqs, iters, lst_size, max_rand, use_bozo, use_slow):

    with open("bozosort_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["inputSize", "delta"])

    with open("slowsort_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["inputSize", "delta"])

    
    for i in range(seqs):
        lib = ctypes.CDLL('./sort_algs.so') 
        lst = []

        for _ in range(lst_size):
            rand_num = random.randint(0, max_rand)
            lst.append(rand_num)

        for _ in range(iters):

            c_array = (ctypes.c_int * lst_size)(*lst)

            if use_bozo == True:
                bozosort_start_time = time.time()
                lib.bozosort(c_array, lst_size)
                bozosort_time = time.time() - bozosort_start_time
                with open('bozosort_data.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([lst_size, "{:.10f}".format(bozosort_time*1000)])

            if use_slow == True:
                bozosort_start_time = time.time()
                lib.bozosort(c_array, lst_size)
                bozosort_time = time.time() - bozosort_start_time
                with open('slowsort_data.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([lst_size, "{:.10f}".format(bozosort_time*1000)])

            if use_slow == False and  use_bozo == False:
                print("Error! no supplied algorithms to run. Please define in function parameters!")
            
        lst_size = lst_size + 1


# Main Program Starts Here:

executeAlgs(seqs = 12, iters = 20, lst_size = 1, max_rand = 100, use_bozo = True, use_slow = True)

