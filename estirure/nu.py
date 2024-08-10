import numpy as np
import matplotlib.pyplot as plt

# Define the bin range
start = 0
end = 10
num_bins = 5

# Create the histogram
data = np.random.uniform(start, end, 1000)
counts, bins, ignored = plt.hist(data, num_bins, edgecolor='black')

# Calculate the middle for x and y
x_middle = (bins[1:] + bins[:-1]) / 2
y_middle = counts

# Plot the marks in the center between start and end of the bin range
plt.scatter(x_middle, y_middle, color='red', marker='x')

# Show the plot
plt.show()
