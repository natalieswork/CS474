import random, os

# Get the current working directory, make file prefix
cwd = os.getcwd()
extension_name = "_data.txt" # Data file extension
file_prefix = cwd + "/rawdata/"
# List of list sizes. There will be a list of size 1 with 1 random number. There will be a list of size 2 with 2 random numbers. Etc.
list_sizes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30,40,50,75,100,125,150,175,200,205,210,220,225,250,300,400,500] 

# Read from list_sizes. Create file n_data.txt, where n is any element of list_sizes.
# Populate the file with n random integers, ranging from 0 to 100. 
try:
    for i in list_sizes:
        file_name = file_prefix + str(i) + extension_name
        with open(file_name, "w") as file:
            for _ in range(i):
                random_number = random.randint(0, 100)
                file.write(str(random_number) + "\n")
    print("\nSuccess!",len(list_sizes),"files were created.\n")

except Exception as e:
    # Handle all exceptions
    print("An error occurred:", e)


