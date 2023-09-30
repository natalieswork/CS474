import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime, os

# Get current working directory
cwd = os.getcwd()

# Load each CSV file into its own dataframe
bozosort_csv_file_path = cwd+"/csvdata/bozosort.csv"
bozo_df = pd.read_csv(bozosort_csv_file_path)
slowsort_csv_file_path = cwd+"/csvdata/slowsort.csv"
slow_df = pd.read_csv(slowsort_csv_file_path)

# Merge both dataframes into one

bozo_df["bozo_time"] = bozo_df["bozo_time"] / 1000
slow_df["slow_time"] = slow_df["slow_time"] / 1000

# Create a plot for lines to go on
plt.figure(figsize=(12, 6))
plt.xlabel("Number of Elements")
plt.ylabel("Time to Sort List (seconds)")
plt.title("Time Complexities: BozoSort vs SlowSort")
plt.legend()

# Plot each data set onto the graph
sns.lineplot(data=bozo_df, x="list_size", y="bozo_time", linewidth=2.5, label="BozoSort")
sns.lineplot(data=slow_df, x="list_size", y="slow_time", label = "SlowSort")

# Save plot to .png
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
plot_filename = f"plot_{current_time}.png"
plt.savefig(cwd+"/plots/"+plot_filename)
