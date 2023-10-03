import matplotlib.pyplot as plt
import numpy as np

# Define a range of input sizes (N)
N_values = [10, 100, 1000, 10000]

# Calculate the corresponding runtimes
runtimes = [N * (np.log(N) / 2) for N in N_values]

# Create the graph
plt.plot(N_values, runtimes, marker='o', linestyle='-')
plt.xlabel('Input Size (N)')
plt.ylabel('Runtime')
plt.title('Runtime Analysis (O(N * log(N)/2))')
plt.grid(True)
plt.savefig("t1.png")


